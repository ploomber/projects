# Directory as entry point

This example shows how you can build a pipeline from a directory with scripts
(without defining a `pipeline.yaml` file).

You can use this sample project structure as a starting template for new
script or notebook-based (just replace the *.py files with *.ipynb) projects.

## Setup environment

~~~sh
conda env create --file environment.yaml
conda activate spec-api-directory
~~~

## Pipeline description

This pipeline contains 5 steps. The last task train a model and outputs a report
and a trained model file. To get the pipeline description:


```bash tags=["bash"]
ploomber status --entry-point '*.py'
```

`--entry-point '*.py'` means "all files with py extension are tasks in the
pipeline". If all the files in the current directory are tasks, you can also
use the shortcut `--entry-point .`.

## Build the pipeline from the command line


```bash tags=["bash"]
mkdir output
ploomber build --entry-point '*.py'
```

Output is stored in the `output/` directory.


## Where to go from here

Building pipelines from a collection of scripts/notebooks without a
`pipeline.yaml` is quick an easy, but has limited features. See the
`spec-api-python` to see how you can declare your tasks in a YAML file.
