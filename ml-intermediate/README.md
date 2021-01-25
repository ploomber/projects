# Intermediate ML project

This example shows how to build an ML pipeline with integration testing (using
the `on_finish` key). When the pipeline takes a lot of time to run end-to-end
it is a good idea to test with a sample, take a look at the `pipeline.yaml`,
`env.yaml` to see how this parametrization happens and how this affects the
`get` function defined in `tasks.py`.

A second spec is provided (`pipeline-serve.yaml`) to show how to use the same
feature engineering code from the training pipeline to serve predictions.

## Setup

~~~bash
# same instructions as the other version
git clone https://github.com/ploomber/projects
cd ml-intermediate

conda env create --file environment.yml
conda activate ml-intermediate
~~~

## Execute the pipeline

```bash tags=["bash"]
ploomber build
```

## Integration testing with a sample

To see available parameters (params parsed from `env.yaml` start with `--env`):

```bash tags=["bash"]
ploomber build --help
```

Run with a sample:

```bash tags=["bash"]
ploomber build --env--sample true 
```

## Serving predictions

Once a model has been trained (by running `ploomber build`), you can run the
serving pipeline with:

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