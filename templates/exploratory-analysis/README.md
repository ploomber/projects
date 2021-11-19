<!-- start header -->
To run this example locally, [install Ploomber](https://ploomber.readthedocs.io/en/latest/get-started/install.html) and execute: `ploomber examples -n templates/exploratory-analysis`

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Ftemplates/exploratory-analysis%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=templates/exploratory-analysis%20issue)

Have questions? [Ask us anything on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/templates/exploratory-analysis/README.ipynb)
<!-- end header -->



# Exploratory Data Analysis

<!-- start description -->
Sample pipeline that explores penguins data.
<!-- end description -->

It contains five tasks, to get, clean, and visualize the data:

<!-- #md -->
```yaml
# Content of pipeline.yaml
tasks:
  # get raw data
  - source: scripts/get.py
    product:
      nb: products/get.html
      data: products/raw.csv

  # quick raw data profiling
  - source: scripts/profile-raw.py
    # html report
    product: products/report-raw.html

  # clean raw data
  - source: scripts/clean.py
    product:
      nb: products/clean.html
      # clean data
      data: products/clean.csv

  # quick clean data profiling
  - source: scripts/profile-clean.py
    # html report     
    product: products/report-clean.html


  # custom plots
  - source: scripts/custom.py
    product: products/custom.html
```
<!-- #endmd -->

Generate the plot (note that this requires `pygraphviz`, you can skip this if you want):

<!-- #md -->
```sh
ploomber plot
```
<!-- #endmd -->


Open the `pipeline.png` file to see the diagram.

## Build pipeline

```sh
ploomber build
```

Each task generates an HTML report, go to the `products/` directory after
building the pipeline to see them.