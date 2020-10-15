from pathlib import Path
import shutil
from glob import iglob
from ploomberutils import process_readme
from invoke import task


@task
def clear(c):
    """Clears output folders
    """
    for f in iglob('*/output'):
        print(f'Deleting contents of: {f}')
        shutil.rmtree(f)
        Path(f).mkdir()


@task
def run_readmes(c):
    """Execute all */README.md files
    """
    for f in iglob('ml-*/README.md'):
        print(f'Processing: {f}')
        process_readme(f)
