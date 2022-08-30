# %%
import sys
from pathlib import Path
import shutil
from glob import iglob

# %%
from invoke import task

# %%
if not Path('LICENSE').exists():
    sys.exit('Error: Run the command from the root folder (the directory '
             'with the LICENSE file).')


# %%
@task
def setup(c, create_conda=True):
    """
    Setup conda env
    """
    cmd = ('eval "$(conda shell.bash hook)"'
           ' && conda env create --file environment.yml --force'
           ' && conda activate projects '
           ' &&') if create_conda else ''

    cmd += (' pip install --editable "_pkg[dev]"'
            ' && pip install --editable templates/python-api/'
            ' && pip install --editable templates/ml-advanced/'
            ' && pip install invoke')

    c.run(cmd)

    c.run('cd spec-api-sql/setup && bash setup.sh')

    print('Done! Activate your environment with:\n' 'conda activate projects')


# %%
@task
def clear(c):
    """Clears output folders
    """
    for f in iglob('*/output'):
        print(f'Deleting contents of: {f}')
        shutil.rmtree(f)
        Path(f).mkdir()

    for f in iglob('*/products'):
        print(f'Deleting contents of: {f}')
        shutil.rmtree(f)
        Path(f).mkdir()

    for f in iglob('*/*.metadata'):
        print(f'Deleting contents of: {f}')
        Path(f).unlink()


# %%
@task
def build(c, name=None, force=False, log=False):
    """See CONTRIBUTING.md for details
    """
    from ploomberutils import nb
    nb.build(name=name, force=force, log=log)
