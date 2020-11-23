from pathlib import Path
import shutil
from glob import iglob
from itertools import chain

import yaml
from invoke import task


@task
def setup(c):
    """
    Setup conda env
    """
    c.run('eval "$(conda shell.bash hook)"'
          ' && conda env create --file environment.yml'
          ' && conda activate projects'
          ' && pip install --editable pkg/'
          ' && pip install --editable python-api/'
          ' && pip install --editable ml-advanced/'
          ' && pip install invoke')  # to be able to run invoke from the env
    print('Done! Activate your environment with:\n' 'conda activate projects')


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
def pre_deploy(c, name=None):
    """
    Pre-deployment (Binder/Deepnote) stuff
    * Execute all */README.md files (to generate */README.ipynb)
    * Generate requirements.txt from environment.yml (for people who don't use conda)
    """
    from ploomberutils import process_readme_md

    if name is None:
        folders = [
            'ml-basic', 'ml-intermediate', 'python-api', 'spec-api-directory',
            'spec-api-python', 'spec-api-r', 'spec-api-sql', 'ml-advanced',
            'etl'
        ]
    else:
        folders = [name]

    process_readme_md(folders + ['.'])

    if name is None:
        pip_deps = list(
            set(chain(*(extract_pip_deps(folder) for folder in folders))))
        reqs = '# This file was automatically generated\n' + '\n'.join(
            pip_deps)
        print('Generating requirements.txt')
        # this file is used by deepnote
        Path('requirements.txt').write_text(reqs)

        # TODO: generate per-example requirements.txt for people not using
        # conda
        conda_deps = list(
            set(chain(*(extract_conda_deps(folder) for folder in folders))))
        conda_deps.remove('pip')
        conda_deps.append({'pip': pip_deps})

        conda = {
            'name': 'projects',
            'channels': ['conda-forge'],
            'dependencies': conda_deps
        }

        conda = '# This file was automatically generated\n' + yaml.dump(conda)
        print('Generating environment.yml')
        # env for binder
        Path('environment.yml').write_text(conda)


def extract_conda_deps(folder):
    with open(Path(folder, 'environment.yml')) as f:
        d = yaml.safe_load(f)

    return d['dependencies'][:-1]


def extract_pip_deps(folder):
    with open(Path(folder, 'environment.yml')) as f:
        d = yaml.safe_load(f)

    return d['dependencies'][-1]['pip']
