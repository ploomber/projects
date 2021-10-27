<!-- start header -->
To run this example locally, execute: `ploomber examples -n cookbook/python-load`.

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fcookbook/python-load%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=cookbook/python-load%20issue)

Have questions? [Ask us anything on Slack.](http://community.ploomber.io/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/cookbook/python-load/README.ipynb)
<!-- end header -->



# Loading pipeline.yaml in Python

<!-- start description -->
Load pipeline.yaml file in a Python session to customize ininitialization.
<!-- end description -->

## Loading the pipeline

Create a function that loads it and returns the DAG object:

<!-- #md -->
```python
# Content of pipeline.py
from ploomber.spec import DAGSpec
from ploomber import with_env


@with_env('env.yaml')
# NOTE: you may add other params to the function, they'll show up in the cli
def make(env):
    dag = DAGSpec('pipeline.yaml', env=dict(env)).to_dag()
    # NOTE: return the DAG, do not call any methods
    return dag

```
<!-- #endmd -->

*Note:* If your pipeline isn't using an `env.yaml` file, simply remove the decorator, and the `env` argument in the function.


## Command-line interface

The CLI will work just as if you were using the `pipeline.yaml` file directly, pass the dotted path to the function in the `--entry-point/-e` argument:

```sh
ploomber status -e pipeline.make
```

```sh
ploomber build -e pipeline.make
```