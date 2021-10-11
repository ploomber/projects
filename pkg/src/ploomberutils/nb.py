import shutil
from pathlib import Path

from ploomber import DAG
from ploomber.tasks import NotebookRunner
from ploomber.products import File
from ploomber.constants import TaskStatus
import nbformat
import jupytext

md_cell = """
*Note:* You can run this example locally (`ploomber examples -n {name}`) or in Binder (hosted JupyterLab ).

[![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252F{name}%252FREADME.ipynb%26branch%3Dmaster)
"""


def process_cell(cell):
    if 'tags' in cell.metadata and 'bash' in cell.metadata.tags:
        cell['source'] = '%%sh\n' + cell['source']
    # jupytext is adding this
    if cell['source'].startswith('%%python'):
        cell['source'] = cell['source'].replace('%%python', '')


def make_task(dag, readme):
    nb = jupytext.read(readme)

    for cell in nb.cells:
        process_cell(cell)

    fmt = nbformat.versions[nbformat.current_nbformat]
    nb.cells.append(fmt.new_code_cell(metadata=dict(tags=['parameters'])))

    source = '\n'.join(c.source for c in nb.cells)

    # if there is no link to binder, add it. Some readmes (like the root one)
    # customize the description for the buttons so we don't add one there
    if 'https://mybinder.org/badge_logo.svg' not in source:
        nb.cells.insert(
            0,
            fmt.new_markdown_cell(source=md_cell.format(
                name=str(readme.parent.name))))

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


def post_process_nb(path):
    nb = jupytext.read(path)

    assert nb.cells[-1].metadata.tags == ['injected-parameters']
    assert nb.cells[-2].metadata.tags == ['parameters']

    nb.cells = nb.cells[:-2]

    jupytext.write(nb, path)


def process_readme_md(folders, parent_dir='.', force=False):
    """
    Process README.md files from given folders, executes them inline
    """
    dag = DAG()

    files = [Path(parent_dir, folder, 'README.md') for folder in folders]

    for f in files:
        make_task(dag, f)

    dag.render()

    # clear the output of tasks that will be executed, otherwise the output
    # from commands such as "ploomber build" will not run anything
    for t in dag.values():
        out = Path(str(t.product)).parent / 'output'
        if t.exec_status == TaskStatus.WaitingExecution and Path(out).exists():
            print(f'Deleting {out}')
            shutil.rmtree(out)

    print(dag.build(force=force))

    for task_name in dag:
        task = dag[task_name]

        if task.exec_status == TaskStatus.Executed:
            post_process_nb(str(task.product))
