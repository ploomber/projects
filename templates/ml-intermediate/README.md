<!-- start header -->
To run this example locally, execute: `ploomber examples -n ml-intermediate`.

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fml-intermediate%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=ml-intermediate%20issue)

Have questions? [Ask us anything on Slack.](http://community.ploomber.io/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/ml-intermediate/README.ipynb)
<!-- end header -->



# Intermediate ML project

Example showing training and serving ML pipelines with integration testing to evaluate training data quality.

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

<!-- #md -->
```yaml
# Content of partial.features.yaml
  name: join
  product: "{{root}}/sample={{sample}}/join.parquet"
  on_finish: integration.no_missing_values
```
<!-- #endmd -->

The function checks that there are no missing values in the data frame. Otherwise, it raises an exception:

<!-- #md -->
```python
# Content of integration.py
import pandas as pd


def no_missing_values(product):
    df = pd.read_parquet(str(product))
    assert not df.isna().sum().sum(), f'Found missing values in {product}'

```
<!-- #endmd -->

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