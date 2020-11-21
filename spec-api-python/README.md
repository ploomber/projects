# Python script-based project

This example shows how you can build script or notebook-based (just replace the
*.py files with *.ipynb) project using a ``pipeline.yaml`` file.

## Setup environment

~~~sh
conda env create --file environment.yaml
conda activate spec-api-python
~~~

## Description

This pipeline contains 3 tasks. The last task generates a plot from the data.

```bash tags=["bash"]
ploomber plot
```

```python
from IPython.display import Image
Image(filename='pipeline.png')
```


To get the pipeline description:

```bash tags=["bash"]
ploomber status
```

## Build the pipeline from the command line

```bash tags=["bash"]
mkdir output
ploomber build
```

Output is stored in the ``output/`` directory.

## Where to go from here

Adding a `pipeline.yaml` file gives you more flexibility to build a pipeline,
if you want to see a more complete example, take a lookt at `ml-basic`. Which
builds a simple Machine Learning pipeline where some of the tasks are Python
functions (instead of scripts).

`spec-api-sql` contains an example where data manipulation starts in a SQL
database, the data is downloaded and visualized using Python.

Using a `pipeline.yaml` file is a convenient way to write your workflows and is
often enough for a lot of projects. However, if you need more flexibility, you
can use the Python API directly, see the `python-api` example.

If you use R, take a look a the `spec-api-r` example, which contains a similar
pipeline to this but using R.
