# Intermediate ML project

Example showing training and serving ML pipelines with integration testing to evaluate training data quality.

## Setup

~~~bash
# conda
conda env create --file environment.yml
conda activate ml-intermediate

# pip
pip install -r requirements.txt
~~~

## Training pipeline

The training pipeline prepares some data (`get`, `sepal-area`, `petal-area`), joins everything into a single file (`join`) and fits a model (`fit`). 

```bash
from ploomber.spec import DAGSpec

dag_train = DAGSpec('pipeline.yaml').to_dag()
dag_train.plot()
```

## Serving pipeline

The serving pipeline gets data that we want to make predictions on, generates the same features we created during training, joins everything into a single file, and makes predictions using a previously trained model.

```bash
dag_serve = DAGSpec('pipeline.serve.yaml').to_dag()
dag_serve.plot()
```

## Integration testing

This example also shows how to use integration testing to evaluate the quality of our data. The `join` task uses the `on_finish` hook, which allows us to run a function when the task finishes execution:

```bash
# note: this is only needed to display a file, you may skip it if running locally
from ploomberutils import display_file
display_file('partial.features.yaml', lines=(10, 13))
```

The function checks that there are no missing values in the data frame. Otherwise it raises an exception:

```bash
display_file('integration.py', syntax='python')
```

## Training a model

To train a model, run:

```sh tags=["bash"]
ploomber build
```

## Serving predictions

Once the model trains, run the serving pipeline with:

```sh tags=["bash"]
ploomber build --entry-point pipeline.serve.yaml
```
