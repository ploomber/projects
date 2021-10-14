<!-- start header -->
To run this example locally, execute: `ploomber examples -n python-api`.

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fpython-api%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=python-api%20issue)

Have questions? [Ask us anything on Slack.](http://community.ploomber.io/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/python-api/README.ipynb)
<!-- end header -->



# Python API

Pipeline project using the Python API.

If you're new to the Python API, check out [python-api-examples/](../python-api-examples) directory, containing tutorials and more examples.

## Description

This pipeline has three tasks:

1. Load task (Python function): CSV file
2. Clean task (Python script):  Jupyter notebook and another CSV file
3. Plot task (Python scripts): Jupyter notebook

## Build

```bash
ploomber build
```