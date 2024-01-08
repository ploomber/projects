<!-- start header -->
To run this locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n templates/exploratory-analysis`


Questions? [Ask us on Slack.](https://ploomber.io/community/)

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


Open the generated file to see the diagram.

## Build pipeline

```sh
ploomber build
```

Each task generates an HTML report, go to the `products/` directory after
building the pipeline to see them.
