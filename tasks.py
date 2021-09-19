from pathlib import Path
import shutil
from glob import iglob
from itertools import chain

import yaml
from invoke import task


@task
def setup(c, create_conda=True):
    """
    Setup conda env
    """
    cmd = ('eval "$(conda shell.bash hook)"'
           ' && conda env create --file environment.yml --force'
           ' && conda activate projects '
           ' &&') if create_conda else ''

    cmd += (' pip install --editable "pkg[dev]"'
            ' && pip install --editable python-api/'
            ' && pip install --editable ml-advanced/'
            ' && pip install invoke')

    c.run(cmd)

    c.run('cd spec-api-sql/setup && bash setup.sh')

    print('Done! Activate your environment with:\n' 'conda activate projects')


@task
def clear(c):
    """Clears output folders
    """
    for f in iglob('*/output'):
        print(f'Deleting contents of: {f}')
        shutil.rmtree(f)
        Path(f).mkdir()

    for f in iglob('*/*.metadata'):
        print(f'Deleting contents of: {f}')
        Path(f).unlink()


@task
def build(c, name=None, run=True, force=False):
    """See CONTRIBUTING.md for details
    """
    from ploomberutils import process_readme_md, readme

    if name == 'readme':
        print('Bulding README.md...')
        Path('README.md').write_text(readme.render())
        folders = []
    elif name is None:
        print('Bulding README.md...')
        Path('README.md').write_text(readme.render())

        exclude = {
            '.',
            'cookbook/grid',
            'cookbook/serialization',
            'cookbook/sql-dump',
            'ml-online',
            'python-api-examples',
        }

        folders = [
            str(Path(path).parent)
            for path in iglob('**/README.md', recursive=True)
            if str(Path(path).parent) not in exclude
        ]

    else:
        folders = [name]

    missing_env_yml = [
        folder for folder in folders
        if not Path(folder, 'environment.yml').exists()
    ]

    if missing_env_yml:
        raise ValueError(f'Missing environment.yml: {missing_env_yml}')

    # Run readme.md to generate readme.ipynb
    if run:
        process_readme_md(folders + ['.'], force=force)

    if name is None:
        pip_deps_by_folder = {
            folder: extract_pip_deps(folder)
            for folder in folders
        }

        save_per_folder_requirements_txt(pip_deps_by_folder)

        pip_deps = sorted(list(set(chain(*pip_deps_by_folder.values()))))
        reqs = '# This file was automatically generated\n' + '\n'.join(
            pip_deps)
        print('Generating requirements.txt')
        # for people not using conda
        Path('requirements.txt').write_text(reqs)

        # TODO: generate per-example requirements.txt for people not using
        # conda
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
        d = yaml.safe_load(f)

    return sorted(d['dependencies'][-1]['pip'])
