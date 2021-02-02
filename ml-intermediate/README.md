# Intermediate ML project

This example shows how to build a training (`pipeline.yaml`) and a serving ML
pipeline (`pipeline-serve.yaml`) that re-uses feature engineering code
`pipeline-features.yaml`, and how to add integration testing (using the `on_finish`
key).

## Setup

~~~bash
# same instructions as the other version
git clone https://github.com/ploomber/projects
cd ml-intermediate

conda env create --file environment.yml
conda activate ml-intermediate
~~~

## Execute the training pipeline

```bash tags=["bash"]
ploomber build --entry-point pipeline.yaml
```

## Serving predictions

Once a model has been trained, you can run the serving pipeline with:

```bash tags=["bash"]
ploomber build --entry-point pipeline-serve.yaml
```

This second pipeline loads some data and uses the model file to make
predictions.

## Where to go from here

Using a `pipeline.yaml` is a convenient way to describe your workflows but it
has some limitations. [`ml-advanced/`](../ml-advanced/README.ipynb) shows a
pipeline written using the Python API, this gives you full flexibility and
allows you to do things such as creating tasks dynamically.

It also shows how to create a Python package to easily share your pipeline and how to test it using `pytest`.