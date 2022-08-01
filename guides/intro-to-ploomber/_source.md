---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.6
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---


# Your first Python pipeline

<!-- start description -->
Introductory tutorial to learn the basics of Ploomber.
<!-- end description -->

## Introduction

Ploomber helps you build modular pipelines. A pipeline (or **DAG**) is a group of tasks with a particular execution order, where subsequent (or **downstream** tasks) use previous (or **upstream**) tasks as inputs.

## Pipeline declaration

This example pipeline contains five tasks, `1-get.py`, `2-profile-raw.py`, 
`3-clean.py`, `4-profile-clean.py` and `5-plot.py`; we declare them in a `pipeline.yaml` file:

<% expand('pipeline.yaml') %>

**Note:** YAML is a human-readable text format similar to JSON.

**Note:** Ploomber supports Python scripts, Python functions, Jupyter notebooks, R scripts, and SQL scripts.

## Opening `.py` files as notebooks

Ploomber integrates with Jupyter. Among other things, it **allows you to open `.py` files as notebooks** (via `jupytext`).

![lab-open-with-nb](https://ploomber.io/images/doc/lab-open-with-notebook.png)

### What sets the execution order?

Ploomber infers the pipeline structure from your code. For example, to
clean the data, we must get it first; hence, we declare the following in `3-clean.py`:

~~~python
# 3-clean.py

# this tells Ploomber to execute the '1-get' task before '3-clean'
upstream = ['1-get']
~~~

## Plotting the pipeline

```bash
ploomber plot
```

```python
from IPython.display import Image
Image(filename='pipeline.png')
```

You can see that our pipeline has a defined execution order.

**Note:** This is a sample predefined five-task pipeline, Ploomber can manage arbitrarily complex pipelines and dependencies among tasks.

## Running the pipeline

```bash
# takes a few seconds to finish
ploomber build
```

This pipeline saves all the output in the `output/` directory; we have the output notebooks and data files:

```bash
ls output
```

## Updating the pipeline

Ploomber automatically caches your pipeline’s previous results and only runs tasks that changed since your last execution.

Execute the following to modify the `3-clean.py` script

```python
from pathlib import Path

path = Path('3-clean.py')
clean = path.read_text()

# add a print statement at the end of 3-clean.py
path.write_text(clean + """
print("hello")
""")
```

Execute the pipeline again:

```bash
# takes a few seconds to finish
ploomber build
```

```python
# restore contents
path.write_text(clean)
```

You'll see that `1-get.py` & `2-profile-raw.py` didn't run because it was not affected by the change!

## Where to go from here

**Bring your own code!** Check out the tutorial to [migrate your code to Ploomber](https://docs.ploomber.io/en/latest/user-guide/refactoring.html).

Have questions? [Ask us anything on Slack](https://ploomber.io/community/).

Want to dig deeper into Ploomber's core concepts? Check out [the basic concepts tutorial](https://docs.ploomber.io/en/latest/get-started/basic-concepts.html).

Want to start a new project quickly? Check out [how to get examples](https://docs.ploomber.io/en/latest/user-guide/templates.html).




