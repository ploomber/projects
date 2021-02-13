"""
Commands to run common tasks: installing dependencies, setup virtual
environment and run tests.

Requires invoke (pip install invoke). For help run "inv -h", to list
commands "inv -l"

Source code for simple commands can be included here, for large ones, save it
in the lib/ folder
"""
from invoke import task
from lib import conda, versioneer


@task
def setup(c):
    """Setup development environment
    """
    print('Creating conda environment...')
    c.run('conda env create environment.yml --force')
    print('Installing package...')
    conda.run_in_env(c, 'pip install --editable .[dev]', env='ml_online')
    print('Done! Activate your environment with: conda activate ml_online')


@task(
    help={
        'inplace':
        'Runs tests in the current environment '
        '(calling pytest directly), otherwise uses nox.'
    })
def test(c, inplace=False):
    """Run tests
    """
    if inplace:
        print('Running tests in the current environment...')
        c.run('pytest tests/', pty=True)
    else:
        c.run('nox', pty=True)


@task
def release(c):
    """Create a new version of this project
    """
    versioneer.release(project_root='.', tag=True)
