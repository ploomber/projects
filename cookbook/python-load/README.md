<!-- start header -->
To run this locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n cookbook/python-load`

[![binder-logo](https://raw.githubusercontent.com/ploomber/projects/master/_static/open-in-jupyterlab.svg)](https://binder.ploomber.io/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fcookbook/python-load%252FREADME.ipynb%26branch%3Dmaster)

Questions? [Ask us on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/cookbook/python-load/README.ipynb)
<!-- end header -->



# Loading pipeline.yaml in Python

<!-- start description -->
Load pipeline.yaml file in a Python session to customize initialization.
<!-- end description -->

## Loading the pipeline

Create a function that loads it and returns the DAG object:

<!-- #md -->
```python
# Content of pipeline.py
from ploomber.constants import TaskStatus
from ploomber.spec import DAGSpec
from ploomber import with_env


@with_env('env.yaml')
# NOTE: you may add extra arguments to the function, they'll show up in the cli
def make(env):
    """Simplest factory function

    Examples
    --------
    Execute in the terminal:
        ploomber build -e pipeline.make
    """
    dag = DAGSpec('pipeline.yaml', env=dict(env)).to_dag()
    # NOTE: a factory function must return a DAG (do not call any methods)
    return dag


@with_env('env.yaml')
def delete_tasks(env):
    """Factory function that deletes tasks based on an input parameter

    Examples
    --------
    Execute in the terminal:
        ploomber build -e pipeline.delete_tasks --env--delete_tasks true
    """
    dag = DAGSpec('pipeline.yaml', env=dict(env)).to_dag()

    if env.delete_tasks:
        del dag['create_another']
        del dag['create_final']

    return dag


@with_env('env.yaml')
def ignore_task_status(env):
    """Factory function that overwrites a task's status and skips it

    Examples
    --------
    Execute in the terminal:
        ploomber task create_file --force
        ploomber build -e pipeline.ignore_task_status --force
    """
    dag = DAGSpec('pipeline.yaml', env=dict(env)).to_dag()
    dag.render()

    # NOTE: this example uses private APIs, and they may not work in the
    # future. Keep an eye on: https://github.com/ploomber/ploomber/issues/681
    # for updates

    # never execute the "create_file" tasl
    dag['create_file']._exec_status = TaskStatus.Skipped
    # this is necessary to prevent ploomber from overwriting the status
    dag._params.cache_rendered_status = True
    return dag

```
<!-- #endmd -->

*Note:* If your pipeline isn't using an `env.yaml` file, remove the decorator and the `env` argument in the function.


## Command-line interface

The CLI will work just as if you were using the `pipeline.yaml` file directly, pass the dotted path to the function in the `--entry-point/-e` argument:

```sh
ploomber status -e pipeline.make
```

To build the pipeline:

```sh
ploomber build -e pipeline.make
```

Note that you can modify values set in the `env.yaml`, to see how, pass ``--help``:

```sh
ploomber build -e pipeline.make --help
```

*Note:* Check out the other functions in `pipeline.yaml` for more examples.
