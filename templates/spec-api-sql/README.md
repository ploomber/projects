<!-- start header -->
To run this locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n templates/spec-api-sql`

Questions? [Ask us on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/templates/spec-api-sql/README.ipynb)
<!-- end header -->




# SQL/Python pipeline

<!-- start description -->
Use SQL scripts to manipulate data in a database, dump a table, and plot it with Python.
<!-- end description -->


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
ploomber plot
```

If running in Jupyter, load the plot with this code:

```python
from IPython.display import Image
Image(filename='pipeline.png')

# NOTE: ploomber plot will generate a pipeline.html (not .png) file if
# pygraphviz is missing. In such case, open the file to view the pipeline plot
```

Otherwise, open the `pipeline.png` file directly.


## Build

```bash
ploomber build
```

The final output is a report: [output/plot.html](output/plot.html).
