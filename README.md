# Ploomber sample projects

![](https://github.com/ploomber/projects/workflows/ci/badge.svg)

This repository contains sample pipelines developed using [Ploomber](github.com/ploomber/ploomber)

## Running examples (no installation needed)

| [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252FREADME.ipynb%26branch%3Dmaster) | [<img src="https://deepnote.com/buttons/launch-in-deepnote-small.svg">](https://deepnote.com/launch?template=deepnote&url=https://github.com/ploomber/projects/blob/master/README.ipynb) |
| ----------- | ----------- |
| No account required | Free account required |
| Might take ~2 mins to load | Loads faster |
| All examples work | ETL example doesn't work yet |


## How to read the examples

Each example contains a `README.md` file with more information, and a
`README.ipynb` file which has the same contents as the `.md` file but in a
Jupyter notebook format and with the output from each cell.

## Where to start?

* Simplest example: [`spec-api-directory/`](spec-api-directory/README.ipynb)
* Machine Learning example: [`ml-basic/`](ml-basic/README.ipynb)
* SQL ETL example: [`spec-api-sql/`](spec-api-sql/README.ipynb)

## Sample projects

### Basic

1. [`spec-api-directory/`](spec-api-directory/README.ipynb) Build a pipeline from of a directory with scripts/notebooks
2. [`spec-api-python/`](spec-api-python/README.ipynb) Pipeline defined using a `pipeline.yaml` spec file
3. [`spec-api-r/`](spec-api-r/README.ipynb) R pipeline defined using a `pipeline.yaml` spec file
4. [`ml-basic/`](ml-basic/README.ipynb) Basic Machine Learning pipeline with a few function tasks and a notebook task for training a model

### Intermediate

5. [`ml-intermediate/`](ml-intermediate/README.ipynb) ML pipeline (Spec API). Similar to `ml-basic/` but shows how to re-use feature engineering code for training and serving and how to add integration tests
6. [`spec-api-sql/`](spec-api-sql/README.ipynb) Pipeline with SQL and Python tasks, using the Spec API
7. [`python-api/`](python-api/README.ipynb) Pipeline using the Python API

### Advanced

8. [`etl/`](etl/README.ipynb) Pipeline with a SQL tasks demonstrating how to extract data from a database and then process it with Python and R
9. [`ml-advanced/`](ml-advanced/README.ipynb) Machine Learning pipeline using the Python API, how to package
your projects so you can install them using `pip install .`, how to test
using `pytest`, how to create an array of experiments to try several models and
run them in parallel.
10. [`ml-online/`](ml-online/README.md) End-to-end machine learning example: training, testing, packaging, and serving predictions using flask.

## User guides

These are part of the User Guide section in the [main documentation](https://ploomber.readthedocs.io/en/stable/user-guide/index.html).

8. [`parametrized/`](parametrized/README.ipynb) Pipeline with input parameters
9. [`debugging/`](debugging/README.ipynb) Pipeline to demonstrate debugging capabilities
10. [`testing/`](testing/README.ipynb) Pipeline with SQL and Python tasks showing how to test pipelines
10. [`sql-templating/`](sql-templating/README.ipynb) SQL pipeline showing how to use macros to write concise SQL scripts