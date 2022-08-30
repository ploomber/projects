# %%
"""
Runs examples from examples/
"""
import os
import pytest
import subprocess
from conftest import _path_to_tests

# %%
_examples = [
    f for f in os.listdir(str(_path_to_tests().parent / 'examples'))
    if f.endswith('.py')
]


# %%
@pytest.mark.parametrize('name', _examples)
def test_examples(tmp_examples_directory, name):
    # TODO: add timeout
    assert subprocess.call(['python', name]) == 0
