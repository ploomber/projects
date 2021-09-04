from functools import wraps
import os
from pathlib import Path
import shutil
import tempfile

import pytest


def _path_to_tests():
    return Path(__file__).absolute().parent


@pytest.fixture
def tmp_directory(tmp_path):
    old = os.getcwd()
    os.chdir(str(tmp_path))
    yield str(Path(tmp_path).resolve())
    os.chdir(old)


def fixture_tmp_dir(source):
    def decorator(function):
        @wraps(function)
        def wrapper():
            old = os.getcwd()
            tmp_dir = tempfile.mkdtemp()
            tmp = Path(tmp_dir, 'content')
            # we have to add extra folder content/, otherwise copytree
            # complains
            shutil.copytree(str(source), str(tmp))
            os.chdir(str(tmp))
            yield tmp
            os.chdir(old)
            shutil.rmtree(tmp_dir)

        return pytest.fixture(wrapper)

    return decorator


@fixture_tmp_dir(_path_to_tests() / '..' / 'examples' / 'pipeline' /
                 'intermediate')
def tmp_intermediate_example_directory():
    pass


@fixture_tmp_dir(_path_to_tests() / '..' / 'examples')
def tmp_examples_directory():
    pass


@fixture_tmp_dir(_path_to_tests() / '..' / 'recipes')
def tmp_recipes_directory():
    pass


@fixture_tmp_dir(_path_to_tests() / '..' / 'examples' / 'pipeline')
def tmp_example_pipeline_directory():
    pass
