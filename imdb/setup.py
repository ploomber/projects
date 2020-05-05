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


NAME = 'imdb_project'

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('src/imdb_project/__init__.py', 'rb') as f:
    VERSION = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name=NAME,
    version=VERSION,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    install_requires=[
        'pandas', 'pyarrow', 'click', 'shap', 'jupyter', 'scikit-learn',
        'ploomber', 'numpydoc', 'matplotlib'
    ],
    extras_require={
        'dev': ['pytest', 'jupytext']
    },
    entry_points={
        # 'console_scripts': [
        #     'power = package.power:main',
        # ]
    },
)
