import io
import re
import ast
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

# read __version__ = VERSION from __init__.py
with open('src/ml_online/__init__.py', 'rb') as f:
    VERSION = str(
        ast.literal_eval(
            _version_re.search(f.read().decode('utf-8')).group(1)))


def read(*names, **kwargs):
    return io.open(join(dirname(__file__), *names),
                   encoding=kwargs.get('encoding', 'utf8')).read()


# NOTE: keep these lists updated as you add more dependencies to your project
# if you rather have any dependency installed via conda, add it here and in
# the environment.yml file

# minimum dependencies for deployment
REQUIRES = [
    'pyarrow',
    'numpy',
    'pandas',
    'ploomber',
    'scikit-learn',
]

# extra dependencies for dewvelopment. e.g. run tests, build docs,
# train new models, generate exploratory notebooks, etc
REQUIRES_DEV = [
    'pytest',
    'nox',
    'pyyaml',
    'invoke',
    'flake8',
    'jupyter',
    'matplotlib',
    'sklearn_evaluation',
]

setup(
    name='ml_online',
    version=VERSION,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    # Include any non-Python files with these extensions, for details:
    # https://setuptools.readthedocs.io/en/latest/userguide/datafiles.html
    package_data={"": ["*/*.sql", "*/*.ipynb", "notebooks/*.py"]},
    install_requires=REQUIRES,
    extras_require={
        'dev': REQUIRES_DEV,
    },
)
