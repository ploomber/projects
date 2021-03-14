# Ploomber sample projects

![](https://github.com/ploomber/projects/workflows/ci/badge.svg)

This repository contains sample pipelines developed using [Ploomber](github.com/ploomber/ploomber)

**Note:** Make sure you read the [first two tutorials](https://ploomber.readthedocs.io/en/stable/get-started/spec-api-python.html) in the documentation to familiarize yourself with Ploomber's basic concepts.

## Running examples (no installation needed)

| [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252FREADME.ipynb%26branch%3Dmaster) | [<img src="https://deepnote.com/buttons/launch-in-deepnote-small.svg">](https://deepnote.com/launch?template=deepnote&url=https://github.com/ploomber/projects/blob/master/README.ipynb) |
| ----------- | ----------- |
| No account required | Free account required |
| Might take ~2 mins to load | Loads faster |
| All examples work | ETL example doesn't work yet |

## How to read the examples

Each example contains a `README.md` file with more information, and a
`README.ipynb` file, which has the same contents as the `.md` file but in a
Jupyter notebook format and with the output from each cell.

## Index

### Basic


1. [`ml-basic/`](ml-basic/README.ipynb) Machine Learning pipeline

2. [`spec-api-r/`](spec-api-r/README.ipynb) R pipeline

3. [`spec-api-directory/`](spec-api-directory/README.ipynb) Pipeline from a directory of scripts


### Intermediate


4. [`ml-intermediate/`](ml-intermediate/README.ipynb) Training and serving ML pipeline with integration testing

5. [`spec-api-sql/`](spec-api-sql/README.ipynb) Pipeline with SQL and Python tasks

6. [`python-api/`](python-api/README.ipynb) Pipeline using the Python API


### Advanced


7. [`ml-online/`](ml-online/README.md) ML pipeline. Train in Kubernetes (via Argo Workflows), deploy using Flask

8. [`etl/`](etl/README.ipynb) SQL pipeline that downloads data, uploads to a database, process it, and plots using Python/R

9. [`ml-advanced/`](ml-advanced/README.ipynb) ML pipeline using the Python API. Shows how to package project, test it using pytest and train models in parallel


## Guides

These are part of the [documentation](https://ploomber.readthedocs.io/en/stable/user-guide/index.html).


1. [`spec-api-python/`](spec-api-python/README.ipynb) Introductory tutorial
2. [`parametrized/`](parametrized/README.ipynb) Pipeline with input parameters
3. [`debugging/`](debugging/README.ipynb) Pipeline to demonstrate debugging capabilities
4. [`testing/`](testing/README.ipynb) Pipeline with SQL and Python tasks showing how to test pipelines
5. [`sql-templating/`](sql-templating/README.ipynb) SQL pipeline showing how to use macros to write concise SQL scripts