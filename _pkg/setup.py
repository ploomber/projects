# %%
import re
import ast
from glob import glob
from os.path import basename, splitext

# %%
from setuptools import find_packages
from setuptools import setup

# %%
_version_re = re.compile(r'__version__\s+=\s+(.*)')

# %%
with open('src/ploomberutils/__init__.py', 'rb') as f:
    VERSION = str(
        ast.literal_eval(
            _version_re.search(f.read().decode('utf-8')).group(1)))

# %%
setup(
    name='ploomberutils',
    version=VERSION,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    # jupyblog pinned mistune>=2, which is incompatible with nbconvert,
    # hence, which ploomber. we are only using some convenient methods from
    # it; we can use 0.0.3
    install_requires=['ploomber', 'click', 'jupyblog<0.0.4'],
    extras_require={
        'dev': [
            # to validate argo specs
            'pyyaml',
            # to extract symbols
            'parso',
        ]
    },
    entry_points={
        'console_scripts': ['ploomberutils=ploomberutils.cli:cli'],
    },
)
