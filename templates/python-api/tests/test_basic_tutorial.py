
import papermill as pm
import jupytext


def test_notebooks(path_to_root):
    source = str(path_to_root / 'notebook.md')
    target = str(path_to_root / 'notebook.ipynb')

    nb = jupytext.read(source)
    jupytext.write(nb, target)

    pm.execute_notebook(target, target, nest_asyncio=True)
