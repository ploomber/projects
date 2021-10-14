import pytest
from pathlib import Path


def _path_to_root():
    return Path(__file__).absolute().parent


@pytest.fixture(scope='session')
def path_to_root():
    return _path_to_root()
