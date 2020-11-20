from pathlib import Path
import shutil
from glob import iglob

from ploomberutils import process_nb_pattern
from invoke import task


@task
def clear(c):
    """Clears output folders
    """
    for f in iglob('*/output'):
        print(f'Deleting contents of: {f}')
        shutil.rmtree(f)
        Path(f).mkdir()

    for f in iglob('*/*.source'):
        print(f'Deleting contents of: {f}')
        Path(f).unlink()


@task
def run_readmes(c):
    """Execute all */README.md files
    """
    process_nb_pattern('*/README.md')
