import papermill as pm
from pathlib import Path
import nbformat
import jupytext


def process_cell(cell):
    if 'tags' in cell.metadata and 'bash' in cell.metadata.tags:
        cell['source'] = '%%sh\n' + cell['source']
    # jupytext is adding this
    if cell['source'].startswith('%%python'):
        cell['source'] = cell['source'].replace('%%python', '')


def process_readme(readme, execute=True):
    nb = jupytext.read(readme)

    for cell in nb.cells:
        process_cell(cell)

    parent = Path(readme).parent
    out = str(parent / 'README.ipynb')

    print('Saving: ', out)
    nbformat.write(nb, out)

    if execute:
        pm.execute_notebook(out, out, kernel_name='python3', cwd=str(parent))
