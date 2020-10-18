from glob import glob
from pathlib import Path

from ploomber import DAG
from ploomber.tasks import NotebookRunner
from ploomber.products import File
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

    print('Saving: ', out)
    nbformat.write(nb, out)

    NotebookRunner(Path(out),
                   File(out),
                   dag,
                   kernelspec_name='python3',
                   name=out,
                   nbconvert_exporter_name='notebook',
                   local_execution=True,
                   papermill_params={'nest_asyncio': True})


def process_readmes():
    dag = DAG()

    files = glob('ml-*/README.md')

    for f in files:
        print(f'Processing: {f}')
        make_task(dag, f)

    dag.build()
