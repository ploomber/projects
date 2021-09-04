"""
Test notebooks in doc/
"""
import shutil
import subprocess
from pathlib import Path
import os

# we have to use this, nbconvert removes cells that execute shell comands
import jupytext

import pytest
from conftest import _path_to_tests

_base = str(_path_to_tests().parent / 'guide')

nbs = [Path(_base, f) for f in os.listdir(_base) if f.endswith('.ipynb')]


# we cannot use papermill since some notebooks use papermill via NotebookRunner
# there is an issue when this happens, so we just run it as scripts using
# ipython directly
def run_notebook(nb):
    print('Running %s' % nb)

    out = 'nb.py'
    jupytext.write(jupytext.read(nb), out)

    # jupytext keeps shell commands but adds them as comments, fix
    lines = []

    for line in Path(out).read_text().splitlines():
        # https://stackoverflow.com/a/29262880/709975
        if line.startswith('# !'):
            line = 'get_ipython().magic("sx %s")' % line[2:]

        lines.append(line)

    Path(out).write_text('\n'.join(lines))

    exit_code = subprocess.call(['ipython', 'nb.py'])

    return exit_code


@pytest.mark.parametrize('nb', nbs, ids=[Path(nb).name for nb in nbs])
def test_guide(nb, tmp_directory):
    # TODO: add timeout
    name = Path(nb).name
    shutil.copy(nb, name)

    assert run_notebook(name) == 0
