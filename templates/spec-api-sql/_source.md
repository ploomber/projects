---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---


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

<% expand('pipeline.yaml') %>

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
