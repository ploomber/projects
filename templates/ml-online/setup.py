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

with open('src/ml_online/__init__.py', 'rb') as f:
    VERSION = str(
        ast.literal_eval(
            _version_re.search(f.read().decode('utf-8')).group(1)))


def read(*names, **kwargs):
    return io.open(join(dirname(__file__), *names),
                   encoding=kwargs.get('encoding', 'utf8')).read()


REQUIRES = [
    # for training models
    'numpy',
    'pandas',
    'ploomber',
    'scikit-learn',
    'jupyter',
    'matplotlib',
    'sklearn_evaluation',
    'pyarrow',

    # for deploying as flask microservice
    'flask',

    # for artifact storage
    'google-cloud-storage',
    'boto3',
]

REQUIRES_DEV = [
    'pytest',
    'invoke',
    'build',
    'wheel',
    'soopervisor',
]

setup(
    name='ml_online',
    version=VERSION,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    install_requires=REQUIRES,
    include_package_data=True,
    extras_require={
        'dev': REQUIRES_DEV,
    },
)
