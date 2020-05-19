import papermill as pm


def test_notebooks(path_to_root):
    nb = str(path_to_root / 'notebook.ipynb')
    pm.execute_notebook(nb, nb, nest_asyncio=True)
