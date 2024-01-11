<!-- start header -->
To run this locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n templates/shell`

Questions? [Ask us on Slack.](https://ploomber.io/community/)

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
