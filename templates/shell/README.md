<!-- start header -->
To run this example locally, [install Ploomber](https://ploomber.readthedocs.io/en/latest/get-started/install.html) and execute: `ploomber examples -n templates/shell`

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Ftemplates/shell%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=templates/shell%20issue)

Have questions? [Ask us anything on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/templates/shell/README.ipynb)
<!-- end header -->



# Executing shell scripts as tasks

*Note: this example requires* `ploomber>=0.13.6`

<!-- start description -->
Create a pipeline with shell scripts as tasks.
<!-- end description -->

## Description

The pipeline has three tasks:

<!-- #md -->
```yaml
# Content of pipeline.yaml
tasks:
  # this script downloads a dataset
  - source: scripts/download.sh
    product: output/data.csv

  # this script plots outputs/data.csv
  - source: scripts/plot.py
    product: output/report.ipynb

  # this script has scripts/download.sh as dependency
  - source: scripts/copy.sh
    product: output/copy.csv
```
<!-- #endmd -->

We download some data, and plot it with Python. We also have a second
shell script that copies the data from the first one to demonstrate how to
declare upstream dependencies.

## Build pipeline

```bash
ploomber build
```