<!-- start header -->
To run this example locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/install.html) and execute: `ploomber examples -n guides/spec-api-python`

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fguides/spec-api-python%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=guides/spec-api-python%20issue)

Have questions? [Ask us anything on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/guides/spec-api-python/README.ipynb)
<!-- end header -->




# Your first Python pipeline

<!-- start description -->
Introductory tutorial to learn the basics of Ploomber.
<!-- end description -->

## Introduction

Ploomber helps you build modular pipelines. A pipeline (or **DAG**) is a group of tasks with a particular execution order, where subsequent (or **downstream** tasks) use previous (or **upstream**) tasks as inputs.

## Pipeline declaration

This example pipeline contains three tasks, `1-get.py`, `2-clean.py`,
and `3-plot.py`; we declare them in a `pipeline.yaml` file:

<!-- #md -->
```yaml
# Content of pipeline.yaml
tasks:
   # source is the code you want to execute (.ipynb also supported)
  - source: 1-get.py
    # products are task's outputs
    product:
      # scripts generate executed notebooks as outputs
      nb: output/1-get.ipynb
      # you can define as many outputs as you want
      data: output/data.csv
    
  - source: 2-clean.py
    product:
      nb: output/2-clean.ipynb
      data: output/clean.csv

  - source: 3-plot.py
    product:
      nb: output/3-plot.ipynb

```
<!-- #endmd -->

**Note:** YAML is a human-readable text format similar to JSON.

**Note:** Ploomber supports Python scripts, Python functions, Jupyter notebooks, R scripts, and SQL scripts.

## Opening `.py` files as notebooks

Ploomber integrates with Jupyter. Among other things, it **allows you to open `.py` files as notebooks** (via `jupytext`).

![lab-open-with-nb](https://ploomber.io/images/doc/lab-open-with-notebook.png)

### How is execution order determined?

Ploomber infers the pipeline structure from your code. For example, to
clean the data, we must get it first; hence, we declare the following in `2-clean.py`:

~~~python
# 2-clean.py

# this tells Ploomber to execute the '1-get' task before '2-clean'
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

**Note:** This is a simple three-task pipeline, but Ploomber can manage arbitrarily complex pipelines and dependencies among tasks.

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

Execute the following to modify the `2-clean.py` script

```python
from pathlib import Path

path = Path('2-clean.py')
clean = path.read_text()

# add a print statement at the end of 2-clean.py
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

You'll see that `1-get.py` didn't run because it was not affected by the change!

## Where to go from here

**Bring your own code!** Check out the tutorial to [migrate your code to Ploomber](https://docs.ploomber.io/en/latest/user-guide/refactoring.html).
<br><br>

Have questions? [Ask us anything on Slack](https://ploomber.io/community/).

Want to dig deeper into Ploomber's core concepts? Check out [the basic concepts tutorial](https://docs.ploomber.io/en/latest/get-started/basic-concepts.html).

Want to start a new project quickly? Check out [how to get examples](https://docs.ploomber.io/en/latest/user-guide/templates.html).
