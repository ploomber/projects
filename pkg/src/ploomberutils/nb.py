import logging
from glob import iglob
import shutil
from pathlib import Path
from itertools import chain
from collections.abc import Mapping

import yaml
from ploomberutils import readme

from ploomber import DAG
from ploomber.tasks import NotebookRunner
from ploomber.products import File
from ploomber.tasks import PythonCallable
from ploomber.executors import Serial
import nbformat
import papermill as pm
import jupytext
from jupyblog.expand import expand
from jupyblog.md import find_metadata_lines, delete_metadata

header_template = """\
<!-- start header -->
To run this example locally, execute: `ploomber examples -n {name}`.

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252F{name}%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title={name}%20issue)

Have questions? [Ask us anything on Slack.](http://community.ploomber.io/)
<!-- end header -->

"""


def front_matter_lines(md):
    try:
        return find_metadata_lines(md)
    except ValueError:
        return (0, 0)


def add_md_header(path, content):
    # if there is no link to binder, add it. Some readmes (like the root one)
    # customize the description for the buttons so we don't add one there
    if 'https://mybinder.org/badge_logo.svg' not in content:
        header = header_template.format(name=str(path.parent))
        _, end = front_matter_lines(content)
        lines = content.splitlines()
        content = '\n'.join(lines[:end + 1] + [header] + lines[end + 1:])

    return content


def process_cell(cell):
    # TODO: remove this
    if 'tags' in cell.metadata and 'bash' in cell.metadata.tags:
        cell['source'] = '%%sh\n' + cell['source']
    # jupytext is adding this
    if cell['source'].startswith('%%python'):
        cell['source'] = cell['source'].replace('%%python', '')


def make_task(dag, readme):
    content = Path(readme).read_text()

    if readme.name == '_source.md':
        pass
    else:
        nb = jupytext.reads(add_md_header(readme, content), fmt='md')
        path_to_expanded = None

    fmt = nbformat.versions[nbformat.current_nbformat]
    nb.cells.append(fmt.new_code_cell(metadata=dict(tags=['parameters'])))

    parent = Path(readme).parent
    preprocessed = str(parent / 'README-preprocessed.ipynb')
    out = str(parent / 'README.ipynb')

    nbformat.write(nb, preprocessed)

    NotebookRunner(
        Path(preprocessed),
        File(out),
        dag,
        kernelspec_name='python3',
        name=parent.name,
        nbconvert_exporter_name='notebook',
        local_execution=True,
        papermill_params={'log_output': True},
        # some readmes contain the %%capture magic which breaks
        # static analysis
        static_analysis=False)

    return path_to_expanded


def _expand_source(product, resources_):
    path_to_source = resources_['path_to_source']
    print(f'Expanding {str(path_to_source)}...')
    path_to_source = Path(path_to_source)
    content = path_to_source.read_text()

    md = expand(
        add_md_header(path_to_source, content),
        root_path=path_to_source.parent,
        template_params=dict(block_start_string='<&',
                             block_end_string='&>',
                             variable_start_string='<%',
                             variable_end_string='%>',
                             comment_start_string='<#',
                             comment_end_string='#>'),
        header='<!-- #md -->',
        footer='<!-- #endmd -->',
    )

    Path(product).write_text(md)


def expand_source(path_to_source, dag):
    path_to_source = Path(path_to_source)
    return PythonCallable(
        _expand_source,
        product=File(path_to_source.parent / '_build' / '_readme_expanded.md'),
        dag=dag,
        name=str(path_to_source),
        params=dict(resources_=dict(path_to_source=str(path_to_source))))


def _execute(upstream, relative_path, product):
    relative_path = Path(relative_path)

    # convert to ipynb
    nb = jupytext.read(upstream.first, fmt='md')

    header = nb.cells[0]['source']
    marks = ['<!-- start header -->\n', '<!-- end header -->\n']

    # verify the readme file contains the header in the first cell
    for mark in marks:
        if mark not in header:
            raise ValueError('Expected first cell to '
                             f'contain a header mark: {mark!r}, got: '
                             f'{header}')

    # remove marks (causes problems with github and nbviewer rendering)
    for mark in marks:
        nb.cells[0]['source'] = nb.cells[0]['source'].replace(mark, '')

    for cell in nb.cells:
        process_cell(cell)

    preprocessed = relative_path / '_build' / 'readme_preprocessed.ipynb'
    jupytext.write(nb, preprocessed)

    if (relative_path / 'products').is_dir():
        shutil.rmtree(relative_path / 'products')

    if (relative_path / 'output').is_dir():
        shutil.rmtree(relative_path / 'output')

    # execute
    pm.execute_notebook(preprocessed,
                        str(product),
                        cwd=str(relative_path),
                        log_output=True)


def execute(relative_path, dag):
    product = Path(relative_path, 'README.ipynb')
    return PythonCallable(_execute,
                          product=File(product),
                          dag=dag,
                          name=str(product),
                          params=dict(relative_path=str(relative_path)))


def _create_readme(upstream, relative_path, product):
    """
    Add README.ipynb in the header and delete front matter
    """
    content = Path(upstream.first).read_text()
    url = ('https://github.com/ploomber/projects/'
           f'blob/master/{relative_path}/README.ipynb')
    link_to_ipynb = ('\nFor a notebook version (with outputs) of this '
                     f'file, [click here]({url})')

    lines = content.splitlines()

    # add link to readme.ipynb at the header
    try:
        end_header = lines.index('<!-- end header -->')
    except ValueError:
        pass
    else:
        lines.insert(end_header, link_to_ipynb)
        content = '\n'.join(lines)

    content = delete_metadata(content)
    Path(product).write_text(content)


def create_readme(relative_path, dag):
    product = Path(relative_path, 'README.md')
    return PythonCallable(_create_readme,
                          product=File(product),
                          dag=dag,
                          name=str(product),
                          params=dict(relative_path=str(relative_path)))


def _make_path(parent_dir, folder):
    if folder == '.':
        return Path(parent_dir, folder, 'README.md')
    else:
        return Path(parent_dir, folder, '_source.md')


def check_file(folders, file):
    missing_env_yml = [
        folder for folder in folders if not Path(folder, file).exists()
    ]

    if missing_env_yml:
        raise ValueError(f'Missing {file}: {missing_env_yml}')


def save_per_folder_requirements_txt(pip_deps_by_folder):
    print('\n')
    for folder, reqs in pip_deps_by_folder.items():
        path = Path(folder, 'requirements.txt')
        print(f'Saving {path}...')
        path.write_text('\n'.join(sorted(reqs)))
    print('\n')


def extract_conda_deps(folder):
    with open(Path(folder, 'environment.yml')) as f:
        d = yaml.safe_load(f)

    return d['dependencies'][:-1]


def extract_pip_deps(folder):
    with open(Path(folder, 'environment.yml')) as f:
        deps = yaml.safe_load(f)

    # this should a dictionary with a single key
    pip_deps = deps['dependencies'][-1]

    if not isinstance(pip_deps, Mapping):
        return []
    else:
        return sorted(pip_deps['pip'])


def write_root_dep_files_and_examples_reqs_txt(folders):
    """
    Write the root environment.yml, root requirements.txt and per example
    requirements.txt from the environment.yml on each example
    """
    pip_deps_by_folder = {
        folder: extract_pip_deps(folder)
        for folder in folders
    }

    # generate requirements.txt for each example
    save_per_folder_requirements_txt(pip_deps_by_folder)

    pip_deps = sorted(list(set(chain(*pip_deps_by_folder.values()))))
    reqs = '# This file was automatically generated\n' + '\n'.join(pip_deps)
    print('Generating requirements.txt')
    # for people not using conda
    Path('requirements.txt').write_text(reqs)

    conda_deps = list(
        set(chain(*(extract_conda_deps(folder) for folder in folders))))
    conda_deps.remove('pip')
    conda_deps = sorted(conda_deps)

    # add nbgitpuller for binder links to work
    conda_deps.append({'pip': sorted(pip_deps + ['nbgitpuller'])})

    conda = {
        'name': 'projects',
        'channels': ['conda-forge'],
        'dependencies': conda_deps
    }

    conda = '# This file was automatically generated\n' + yaml.dump(conda)
    print('Generating environment.yml')
    # env for binder
    Path('environment.yml').write_text(conda)

    # export to binder env repo
    Path('../binder-env/environment.yml').write_text(conda)


def make(name=None, parent_dir='.', force=False):
    """
    Process _source.md files from given folders, executes them inline
    """
    if not name:
        exclude = {
            # root readme is built differently
            '.',
            'python-api-examples',
        }

        # find all folders
        folders = [
            str(Path(path).parent)
            for path in iglob('**/_source.md', recursive=True)
            if str(Path(path).parent) not in exclude
        ]

        write_root_dep_files_and_examples_reqs_txt(folders)
    else:
        folders = [name]

    dag = DAG(executor=Serial(build_in_subprocess=False))

    paths = [
        _make_path(parent_dir, folder) for folder in folders if folder != '.'
    ]

    tasks_expand = [expand_source(path, dag) for path in paths]

    for task_expand in tasks_expand:
        relative_path = str(Path(task_expand.name).parent)
        task_create = create_readme(relative_path, dag)
        task_execute = execute(relative_path, dag)
        task_expand >> task_create
        task_expand >> task_execute

    if not name:
        readme.render(dag) >> readme.execute(dag)

        # check they all have an environment.yml and requirements.txt
        check_file(folders, 'environment.yml')
        check_file(folders, 'requirements.txt')

    return dag


def build(name=None, parent_dir='.', force=False, log=False):
    if log:
        logging.basicConfig(level=logging.INFO)

    dag = make(name=name, parent_dir=parent_dir, force=force)

    print(dag.build(force=force))

    print('Done. If the environment.yml needs to be built again, '
          'push changes from the binder-env repository.')
