<!-- start header -->
To run this example locally, execute: `ploomber examples -n spec-api-sql`.

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fspec-api-sql%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=spec-api-sql%20issue)

Have questions? [Ask us anything on Slack.](http://community.ploomber.io/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/spec-api-sql/README.ipynb)
<!-- end header -->




# SQL/Python pipeline

Pipeline with SQL and Python tasks.

## Create sample data


```bash
# create sample data
cd setup
bash setup.sh
# move back to the original spec-api-sql folder
cd ..
```

## Definition

<!-- #md -->
```yaml
# Content of pipeline.yaml
meta:
  product_default_class:
    SQLScript: SQLiteRelation

  jupyter_hot_reload: True

config:
  hot_reload: True

clients:
  # tasks
  SQLScript: config.get_client
  SQLDump: config.get_client
  # products
  SQLiteRelation: config.get_client

tasks:
  - source: filter_sales.sql
    product: [filtered_sales, table]
    name: filter_sales

  - source: group_sales.sql
    product: [grouped_sales, table]
    name: group_sales

  - source: filter_prices.sql
    product: [filtered_prices, table]
    name: filter_prices

  - source: join.sql
    product: [joined, table]
    name: join

  - class: SQLDump
    source: join_dump.sql
    product: output/joined_data.csv
    name: join_dump
    chunksize: null

  - source: plot.py
    product: output/plot.html
```
<!-- #endmd -->

The first two sections configure our pipeline; the `tasks` section is the
actual pipeline definition. First, we see that we have a few SQL transformations,
then we dump a table into a CSV file and produce an HTML report at the end.
The order here doesn't matter, the source code itself declares its upstream dependencies, and Ploomber extracts them to execute your pipeline.


## Plot

```bash
# Note: if plotting locally, install pygrapviz first
ploomber plot
```

If running in Jupyter, load the plot with this code:

```python
from IPython.display import Image
Image(filename='pipeline.png')
```

Otherwise, open the `pipeline.png` file directly.


## Build

```bash
ploomber build
```

The final output is a report: [output/plot.html](output/plot.html).