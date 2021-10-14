import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--force",
        action="store_true",
        default=False,
        help="Force build"
    )


@pytest.fixture
def force(request):
    return request.config.getoption("--force")
