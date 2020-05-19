from pathlib import Path
from glob import glob
from conftest import _path_to_root
import pytest
import papermill as pm

path_to_root = _path_to_root()

nbs = [Path(f) for f in glob(str(Path(path_to_root, '**', 'notebook.ipynb')))]


@pytest.mark.parametrize('nb', nbs)
def test_notebooks(nb, tmp_path):
    pm.execute_notebook(nb, tmp_path / nb.parent.name + '.ipynb',
                        cwd=tmp_path,
                        nest_asyncio=True)
