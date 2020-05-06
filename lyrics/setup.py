"""
Minimal setup.py

References
----------
Built using: https://github.com/ploomber/template
setup.py reference: https://setuptools.readthedocs.io/en/latest/setuptools.html
More on pkg structure: https://blog.ionelmc.ro/2014/05/25/python-packaging/
Sample setup.py with explanations: https://github.com/pypa/sampleproject/blob/master/setup.py

Notes
-----
* Only files under src/ (and a few special files) are expected requirements for
    deployment, everything else is expected for development/testing purposes,
    hence not included in a source or built distribution

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

with open('src/ploomber_lyrics/__init__.py', 'rb') as f:
    VERSION = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


# NOTE: keep these lists updated as you add more dependencies to your project
# if you rather have any dependency installed via conda, add it here and in
# environment.yml


# Minimum needed to execute this project, this subset should be enough
# to run the pipeline in production
REQUIRES = []
# Extra packages for running tests, install with: pip install ".[test]"
REQUIRES_TEST = ['pytest', 'nox']
# For developers (e.g. train a new model, run exploratory notebooks)
REQUIRES_DEV = ['pyyaml']
# To build documentation
REQUIRES_DOC = []

setup(
    name='ploomber_lyrics',
    version=VERSION,

    # Automatically find packages under src/
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],

    # Include any files in any package with these extensions
    # NOTE: for these files to be included, they have to be inside a proper
    # module (there has to be an __init__.py file)
    package_data={"": ["*.txt", "*.rst", "*.sql", "*.ipynb"]},

    install_requires=REQUIRES,
    # Extra dependencies, only needed in specific cases
    extras_require={
        'dev': REQUIRES_DEV,
        'test': REQUIRES_DEV + REQUIRES_TEST,
        'doc': REQUIRES_DEV + REQUIRES_DOC,
        'all': REQUIRES_TEST + REQUIRES_DEV + REQUIRES_DOC
    },
    # if your pipeline requires packages at setup time (e.g. creates C
    # extensions), you also need to provide setup_requires, see setuptools
    # documentation for details
    setup_requires=[],
    # Entry points are useful for providing a CLI interface to your pipeline:
    # e.g. $ ploomber_lyrics run
    entry_points={},
)
