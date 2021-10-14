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

# Intermediate ML project

<!-- start description -->
Training and serving ML pipelines with integration testing to evaluate training data quality.
<!-- end description -->

## Training pipeline

The training pipeline prepares some data (`get`, `sepal-area`, `petal-area`), joins everything into a single file (`join`), and fits a model (`fit`). 

```python
from ploomber.spec import DAGSpec

dag_train = DAGSpec('pipeline.yaml').to_dag()
dag_train.plot()
```

## Serving pipeline

The serving pipeline gets data that we want to make predictions on, generates the same features we created during training, joins everything into a single file, and makes predictions using a previously trained model.

```python
dag_serve = DAGSpec('pipeline.serve.yaml').to_dag()
dag_serve.plot()
```

## Integration testing

This example also shows how to use integration testing to evaluate the quality of our data. The `join` task uses the `on_finish` hook, which allows us to run a function when the task finishes execution:

<% expand('partial.features.yaml', lines=(10, 13)) %>

The function checks that there are no missing values in the data frame. Otherwise, it raises an exception:

<% expand('integration.py') %>

## Training a model

To train a model, run:

```sh
ploomber build
```

## Serving predictions

Once the model trains, run the serving pipeline with:

```sh
ploomber build --entry-point pipeline.serve.yaml
```
