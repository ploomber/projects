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

**Note:** This tutorial is a quick introduction. If you want
to learn about Ploomber's core concepts and design rationale, go to the
[the next tutorial](https://ploomber.readthedocs.io/en/latest/get-started/basic-concepts.html).


## Introduction

A pipeline (or **DAG**) is a group of tasks with a particular execution order, where subsequent (or **downstream** tasks) use previous (or **upstream**) tasks as inputs.

This example pipeline contains three tasks, `1-get.py`, `2-clean.py`, and `3-plot.py`.

**Note:** These tasks are Python scripts, but you can use Python functions, Jupyter notebooks, R scripts and SQL scripts.

**Note:** This is a simple three-task pipeline, but Ploomber can manage arbitrarily complex pipelines and dependencies among tasks.

## Integration with Jupyter

Ploomber integrates with Jupyter. If you open the scripts inside the
`jupyter notebook` app, they will render as notebooks. If you're using `jupyter lab`, you need to right click -> open with -> Notebook as shown below:

![lab-open-with-nb](https://ploomber.io/images/doc/lab-open-with-notebook.png)

**Note**: `.ipynb` files are also supported.

Along with the `*.py` files, there is a `pipeline.yaml` file where we declare which files we use as tasks:

<% expand('pipeline.yaml') %>

**Note:** YAML is a human-readable text format similar to JSON; Ploomber uses it to describe the tasks in our pipeline.

### How is execution order determined?

Ploomber infers the pipeline structure from your code. For example, to
clean the data, we must get it first; hence, we declare the following in `2-clean.py`:

~~~python
# this tells Ploomber to execute the '1-get' task before '2-clean'
upstream = ['1-get']
~~~

## Lets plot the pipeline
Let's plot the pipeline:

```bash
ploomber plot
```

```python
from IPython.display import Image
Image(filename='pipeline.png')
```

You can see that our pipeline has a defined execution order: `1-get` -> `2-clean` -> `3-plot`.

## Running the pipeline

Let's run the pipeline:

```bash
# takes a few seconds to finish
ploomber build
```

This pipeline saves all the output in the `output/` directory; we have a few
data files and the output notebooks:

```bash
ls output
```


## Updating the pipeline

Ploomber automatically cache your pipeline’s previous results, and only runs tasks that changed since your last execution. 
To see how it works, execute the following to modify the `2-clean.py` script

```python
from pathlib import Path

path = Path('2-clean.py')
clean = path.read_text()
path.write_text(clean + '\nprint("hello")')
```

Let's now build again:

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

**Bring your own code!** Check out the refactoring tutorial [create your own pipeline](https://docs.ploomber.io/en/latest/user-guide/refactoring.html)
<br><br>

Want to dig deeper into Ploomber's core concepts? Check out [the basic concepts tutorial](https://ploomber.readthedocs.io/en/latest/get-started/basic-concepts.html).

Want to take a look at some examples? Check out how to [download templates](https://ploomber.readthedocs.io/en/latest/user-guide/templates.html).

Have questions? [Ask us anything on Slack](https://ploomber.io/community/).

