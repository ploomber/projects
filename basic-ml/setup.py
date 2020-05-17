"""
Minimal setup.py

Blog post on Python packaging: https://ploomber.io/posts/packaging/

Built using: https://github.com/ploomber/template
setup.py reference: https://setuptools.readthedocs.io/en/latest/setuptools.html
More on pkg structure: https://blog.ionelmc.ro/2014/05/25/python-packaging/
"""
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

with open('src/basic_pipeline/__init__.py', 'rb') as f:
    VERSION = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='basic_pipeline',
    version=VERSION,
    description=None,
    license=None,
    author=None,
    author_email=None,
    url=None,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    package_data={"": ["*.txt", "*.rst", "*.sql", "*.ipynb"]},
    classifiers=[],
    keywords=[],
    install_requires=[
        'ploomber==0.2.1',
        'pandas==1.0.1',
        'scikit-learn==0.22.1', 'joblib==0.14.1',
        'pyarrow==0.16.0'],
    extras_require={},
    entry_points={},
)
