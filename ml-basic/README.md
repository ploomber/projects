# Basic ML project

This example shows how to build a Machine Learning pipeline using the Spec API.

Take a look at the `pipeline.yaml` for more details.

## Setup

Make sure you are in the `ml-basic` folder.

~~~bash
# setup environment
conda env create --file environment.yml
conda activate ml-basic
~~~

## Execute the pipeline

```bash tags=["bash"]
# make sure output folder exists
mkdir output

# execute using the spec file
ploomber build --entry-point pipeline.yaml
```

Note: `ploomber build` also works because Ploomber looks for a `pipeline.yaml` file by default.