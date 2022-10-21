<!-- start header -->
To run this locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n templates/python-api`

[![binder-logo](https://raw.githubusercontent.com/ploomber/projects/master/_static/open-in-jupyterlab.svg)](https://binder.ploomber.io/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Ftemplates/python-api%252FREADME.ipynb%26branch%3Dmaster)

Questions? [Ask us on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/templates/python-api/README.ipynb)
<!-- end header -->



# Python API

<!-- start description -->
Loads, clean, and plot data using the Python API.
<!-- end description -->


If you're new to the Python API, check out [python-api-examples/](../../python-api-examples) directory, containing tutorials and more examples.

## Description

This pipeline has three tasks:

1. Load task (Python function): CSV file
2. Clean task (Python script):  Jupyter notebook and another CSV file
3. Plot task (Python scripts): Jupyter notebook

## Setup

```sh
pip install -r requirements.txt
pip install --editable .
```

## Build

```bash
ploomber build
```
