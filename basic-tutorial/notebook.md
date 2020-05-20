---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
import importlib
from pathlib import Path
from IPython.display import Image, HTML, Markdown, display
from ploomber_basic import pipeline
```
# Ploomber tutorial

This example project showcases the basic Ploomber experience, hopefully, this interactive tutorial will convince you to try out Ploomber in your next Data Science project.

Let's imagine you already have a Ploomber pipeline, which is organized in a few tasks. Ploomber allows you to quickly iterate by keeping track of source code changes and skipping unnecessary computations.

Let's first retrieve our pipeline:

```python
dag = pipeline.make()
```

Plotting it makes easy to understand dependencies between tasks, each node corresponds to one.

```python
Image(filename=dag.plot())
```

<!-- #region -->
From the diagram above we can see that running our pipeline will generate a few things:

1. Load task (Python function): generates a CSV file
2. Clean task (Jupyter notebook): the notebook itself and another CSV file
3. Plot task (Jupyter notebook): the notebook itself


The pipeline structure implies that load is a dependency for clean, and clean is a dependency for plot. Given such specification, Ploomber knows that it has to run load, clean and plot, in that order. Furthermore, when clean is executed, Ploomber will automatically insert the output from load at runtime, this ensures that you are running your code with the right inputs (there are no hardcoded paths in any of the tasks).

Let's run it now:
<!-- #endregion -->

```python
dag.build()
```

<!-- #region -->
You can take a look at the generated output by [clicking here](output/), take a look at the notebooks, they are just like our Python scripts but in Jupyter notebook format, which makes easy to embed tables and plots, while we keep our source code clean in Python scripts.


Let's see what happens if we build again:
<!-- #endregion -->

```python
dag.build()
```

It didn't run anything! That's because our pipeline has not changed, there is nothing to run. Skipping unnecessary computations can save you a lot of time, especially when tasks take a lot to run. Our example is a simple, linear graph, but Ploomber works even when your pipeline has a lot of tasks with multiple dependencies.

The `dag` object is a fully interactive way of exploring our pipeline. Let's use it to know where our code is located:

```python
# get list of task names
list(dag)
```

```python
# get task
task = dag['load']
```

```python
# where is this code declared?
print(task.source.loc)
```

Let's modify the code to see how Ploomber handles the change.

For example, replace the line:

<!-- #md -->

```python
df['x'] = df['x'] = 1
```

With:

```python
df['x'] = df['x'] = 42
```

<!-- #endmd -->

[Click here to open functions.py](src/ploomber_basic/functions.py)


Then come back and run:

```python
dag.build()
```

You should see that all three tasks ran, that's because the load function is the root node. Let's try with another task:

```python
print(dag['clean.py'].source.loc)
```

Go ahead and modify the file.

[Click here to open clean.py](src/ploomber_basic/notebooks/clean.py)

Then run:

```python
dag.build()
```

<!-- #region -->
You should see that Ploomber skipped the load task since the clean task is not a dependency.

Ploomber also provides a convenient way to debug tasks. Imagine we found and error in our load step and we want to see what's going on, we can easily do so by starting a debugging session.

Try it out by typing:

```python
dag['load'].debug()
```

in the cell below.

<!-- #endregion -->

```python
# Remove the comment from the line below, a new prompt will appear
# dag['load'].debug()
```

Type `n` and press enter to move to the next line, `q` and enter to quit.

**Tip**: Try running `n` once to move to the second line, then `df` to print the data frame contents.

Let's take a look at the actual pipeline declaration, where we'll find a bunch of interesting things.

```python
Markdown("""
```python
{}
```
""".format(Path(pipeline.__file__).read_text()))
```

You've made it to the end of this tutorial. Hopefully this will convince you to give it a try in your next project. Ploomber is much more than executing functions and scripts. It also handles SQL scripts pretty well, allows you to test the output of each task, handle configuration settings and much more!

Don't hesitate with any questions you might have. Feel free to [open an issue](https://github.com/ploomber/ploomber/issues/new) in the repository. Thanks for reading!

## Where to go from here

* Take a look at our [documentation](https://ploomber.readthedocs.io/en/stable/)
* Dive into our [codebase](https://github.com/ploomber/ploomber)
