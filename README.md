# Ploomber sample projects

![CI](https://github.com/ploomber/projects/workflows/ci/badge.svg)

<p align="center">
  <a href="https://ploomber.io/community">Join our community</a>
  |
  <a href="https://www.getrevue.co/profile/ploomber">Newsletter</a>
  |
  <a href="https://ploomber.readthedocs.io/">Docs</a>
  |
  <a href="https://twitter.com/intent/user?screen_name=ploomber">Twitter</a>
  |
  <a href="https://ploomber.io/">Blog</a>
  |
  <a href="https://www.youtube.com/channel/UCaIS5BMlmeNQE4-Gn0xTDXQ">YouTube</a>
  |
  <a href="mailto:contact@ploomber.io">Contact us</a>
</p>

This repository contains sample pipelines developed using [Ploomber](https://github.com/ploomber/ploomber).

**Note:** We recommend you to go through the [first tutorial](https://ploomber.readthedocs.io/en/latest/get-started/spec-api-python.html) to learn the basics of Ploomber.

## Running examples

Use Binder (free, hosted JupyterLab):

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252FREADME.ipynb%26branch%3Dmaster)

Or run locally:

~~~sh
pip install ploomber

# list examples
ploomber examples

# download example with name
ploomber examples --name {name}

# example
ploomber examples --name templates/mlflow
~~~

## How to read the examples

Each example contains a `README.md` file that describes it; a `README.ipynb` is also available with the same contents but in Jupyter notebook format and with command outputs. In addition, files for `pip` (`requirements.txt`) and  `conda` (`environment.yml`) are provided for local execution.

## Index

### Templates

Starting points for common use cases. Use them to ramp up a project quickly.


1. [`templates/etl`](templates/etl/README.ipynb) Download a data file, upload it to a database, process it, and plot with Python and R.

2. [`templates/exploratory-analysis`](templates/exploratory-analysis/README.ipynb) Sample pipeline that explores penguins data.

3. [`templates/ml-advanced`](templates/ml-advanced/README.ipynb) ML pipeline using the Python API. Shows how to create a Python package, test it with pytest, and train models in parallel.

4. [`templates/ml-basic`](templates/ml-basic/README.ipynb) Download data, clean it, generate features and train a model.

5. [`templates/ml-intermediate`](templates/ml-intermediate/README.ipynb) Training and serving ML pipelines with integration testing to evaluate training data quality.

6. [`templates/ml-online`](templates/ml-online/README.ipynb) Load data, generate features, train a model, and deploy model with flask.

7. [`templates/mlflow`](templates/mlflow/README.ipynb) Train a grid of models and log them to MLflow.

8. [`templates/python-api`](templates/python-api/README.ipynb) Loads, clean, and plot data using the Python API.

9. [`templates/shell`](templates/shell/README.ipynb) Create a pipeline with shell scripts as tasks.

10. [`templates/spec-api-directory`](templates/spec-api-directory/README.ipynb) Create a pipeline from a directory with scripts (without a pipeline.yaml file).

11. [`templates/spec-api-r`](templates/spec-api-r/README.ipynb) Load, clean and plot data with R.

12. [`templates/spec-api-sql`](templates/spec-api-sql/README.ipynb) Use SQL scripts to manipulate data in a database, dump a table, and plot it with Python.


### Cookbook

Short and to-the-point examples showing how to use a specific feature.


1. [`cookbook/dynamic-params`](cookbook/dynamic-params/README.ipynb) Pipeline parameters whose values are computed at runtime.

2. [`cookbook/grid`](cookbook/grid/README.ipynb) An example showing how to create a grid of tasks to train models with different parameters.

3. [`cookbook/python-load`](cookbook/python-load/README.ipynb) Load pipeline.yaml file in a Python session to customize ininitialization.

4. [`cookbook/serialization`](cookbook/serialization/README.ipynb) Shows how to use the serializer and unserializer decorators.

5. [`cookbook/sql-dump`](cookbook/sql-dump/README.ipynb) A minimal example showing how to dump a table from a SQL database.

6. [`cookbook/variable-number-of-products`](cookbook/variable-number-of-products/README.ipynb) Shows how to create tasks whose number of products depends on runtime conditions.


### Guides

In-depth tutorials for learning.  These are part of the [documentation](https://ploomber.readthedocs.io/en/latest/user-guide/index.html).


1. [`guides/debugging`](guides/debugging/README.ipynb) Tutorial showing techniques for debugging pipelines.

2. [`guides/logging`](guides/logging/README.ipynb) Tutorial showing how to add logging to a pipeline.

3. [`guides/parametrized`](guides/parametrized/README.ipynb) Tutorial showing how to parametrize pipelines and change parameters from the command-line.

4. [`guides/refactor`](guides/refactor/README.ipynb) Using Soorgeon to convert a notebook into a Ploomber pipeline.

5. [`guides/serialization`](guides/serialization/README.ipynb) Tutorial explaining how the serializer and unserializer fields in a pipeline.yaml file work.

6. [`guides/spec-api-python`](guides/spec-api-python/README.ipynb) Introductory tutorial to learn the basics of Ploomber.

7. [`guides/sql-templating`](guides/sql-templating/README.ipynb) Introductory tutorial teaching how to develop modular SQL pipelines.

8. [`guides/testing`](guides/testing/README.ipynb) Tutorial showing how to use a task's on_finish hook to test data quality.



## Python API

The simplest way to get started with Ploomber is via the Spec API, which allows you to describe pipelines using a `pipeline.yaml` file, most examples on this repository use the Spec API. However, if you want more flexibility, you may write pipelines with Python.

The [`templates/python-api/`](templates/python-api) directory contains a project written using the Python API. And the [`python-api-examples/`](python-api-examples) includes some tutorials and more examples.