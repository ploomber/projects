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

```python
import os
from pathlib import Path
import shutil

from IPython.display import Image
```

# Notebook refactoring

<!-- start description -->
Using Soorgeon to convert a notebook into a Ploomber pipeline.
<!-- end description -->

[Soorgeon](https://github.com/ploomber/soorgeon) is a tool from the Ploomber ecosystem that allows you to convert monolithic notebooks into maintainable pipelines.

We have to examples, an exploratory data analysis notebook (`eda.ipynb`), and a Machine Learning notebook (`ml.ipynb`).

## Refactoring `eda.ipynb`

Before we proceed, open `eda.ipynb` to see how the code looks like, you'll notice that we have three sections (load, clean, and plot). Soorgeon uses H2 markdown headings to determine where to split the tasks in the output pipeline.

Let's execute the refactoring command:

```sh
soorgeon refactor eda.ipynb
```

Let's generate the pipeline diagram (note: if you're running this locally, you must install `pygraphviz` first):

```sh
ploomber plot
```

```python
Image('pipeline.png')
# NOTE: ploomber plot will generate a pipeline.html (not .png) file if
# pygraphviz is missing. In such case, open the file to view the pipeline plot
```

We can see that `soorgeon refactor` generated a Ploomber pipeline with one task per notebook section. The source code for each task is in the `tasks/` folder:

```python
print('\n'.join(os.listdir('tasks')))
```

Each task is a `.py` file, however, as with any other Ploomber pipeline, you can open those scripts as notebooks by doing `Right click -> Open With -> Notebook`.

The command also generates a `pipeline.yaml` file, which is the file Ploomber uses to read your pipeline:

```python
print(Path('pipeline.yaml').read_text())
```

Let's run the pipeline:

```sh
ploomber build
```

Let's now refactor a more complex notebook.

```python
# clean up the files from this pipeline
if Path('tasks').exists():
    shutil.rmtree('tasks')

if Path('output').exists():
    shutil.rmtree('output')
    
if Path('pipeline.yaml').exists():
    Path('pipeline.yaml').unlink()
```

## Refactoring `ml.ipynb`

`ml.ipynb` is a Machine Learning pipeline that prepares a training set and then trains two models, let's refactor it:

```sh
soorgeon refactor ml.ipynb
```

Let's see the diagram:

```sh
ploomber plot
```

```python
Image('pipeline.png')
```

We see that `soorgeon refactor` accurately determined the dependencies among sections, even identifying that the model training tasks (`linear-regression` and `random-forest-regressor`) are independent of each other and can run in parallel.

Let's run the pipeline:

```sh
ploomber build
```

That's it! Now give it a try with one of your notebooks!
