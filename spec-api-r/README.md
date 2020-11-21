# Python script-based project

This example shows how you can build script or notebook-based (just replace the
*.R files with *.ipynb) project using a ``pipeline.yaml`` file.

To execute the pipeline, first, open a terminal session, then move to this
folder:

## Setup environment

(Note: Only required if you are running this example in your computer, not
required if using Binder/Deepnote)

~~~sh
conda env create --file environment.yaml
conda activate spec-api-python
~~~

## Pipeline description

This pipeline contains 3 tasks. The last task generates a plot. To get the
pipeline description:

```bash tags=["bash"]
ploomber status
```

## Build the pipeline from the command line

```bash tags=["bash"]
mkdir output
ploomber build
```

Output is stored in the ``output/`` directory.
