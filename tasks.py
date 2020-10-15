from glob import iglob
from ploomberutils import process_readme
from invoke import task


@task
def clear(c):
    """Clears output folders
    """
    for f in iglob('*/output'):
        print(f'Processing: {f}')


@task
def run_readmes(c):
    """Execute all */README.md files
    """
    for f in iglob('ml-*/README.md'):
        print(f'Processing: {f}')
        process_readme(f)
