from pathlib import Path

from ploomber import DAG
from ploomber.tasks import NotebookRunner
from ploomber.products import File
from ploomber.constants import TaskStatus
import nbformat
import jupytext


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

    parent = Path(readme).parent
    out = str(parent / 'README.ipynb')

    nbformat.write(nb, out)

    NotebookRunner(Path(out),
                   File(out),
                   dag,
                   kernelspec_name='python3',
                   name=out,
                   nbconvert_exporter_name='notebook',
                   local_execution=True)


def post_process_nb(path):
    nb = jupytext.read(path)

    assert nb.cells[-1].metadata.tags == ['injected-parameters']
    assert nb.cells[-2].metadata.tags == ['parameters']

    nb.cells = nb.cells[:-2]

    jupytext.write(nb, path)


def process_readme_md(folders):
    """
    Process README.md files from given folders, executes them inline
    """
    dag = DAG()

    files = [Path(folder, 'README.md') for folder in folders]

    for f in files:
        make_task(dag, f)

    dag.build()

    for task_name in dag:
        task = dag[task_name]

        if task.exec_status == TaskStatus.Executed:
            post_process_nb(str(task.product))
