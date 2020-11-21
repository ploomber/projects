import jupytext
from pathlib import Path
import shutil
from glob import iglob

from invoke import task


@task
def setup(c):
    """
    Setup conda env
    """
    with c.cd('pkg'):
        c.run('eval "$(conda shell.bash hook)" '
              '&& conda env create --file environment.yml '
              '&& pip install --editable .'
              '&& pip install invoke')  # to be able to run invoke from the env
    print('Done! Activate your environment with:\n'
          'conda activate ploomber_projects')


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
def pre_deploy(c, pattern='*/README.md'):
    """
    Pre-deployment (Binder/Deepnote) stuff
    * Execute all */README.md files (to generate */README.ipynb)
    * Generate requirements.txt from environment.yml (for people who don't use conda)
    """
    from ploomberutils import process_nb_pattern
    process_nb_pattern(pattern)


# TODO: generate requirements.txt for people not using conda


@task
def deepnote(c):
    """
    Export README.md to deepnote_home.ipynb, which is the displayed file when
    launchign the project to Deepnote
    """
    nb = jupytext.read('README.md')
    jupytext.write(nb, 'deepnote_home.ipynb')
