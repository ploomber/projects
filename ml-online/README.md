# Online API

This example shows and end-to-end machine learning project using Ploomber.

Requires [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

Note: all commands must be executed in the `ml-online/` directory.

## Setup development environment

```sh
# required to run cli commands
pip installl invoke

# if using conda
invoke setup
# activate environment
conda activate ml-online

# otherwise use pip directly
pip install -r requirements.txt
pip install --editable .
```

## Training pipeline

Get a summary of the training pipeline:

```sh
ploomber status
```

Run training pipeline:

```sh
ploomber build
```

Output from the training pipeline saved in the `products/` folder.

## Online API

Copy the trained model inside the project's package:

```sh
cp products/model.pickle src/ml_online/model.pickle
```

Start web application:

```sh
export FLASK_APP=ml_online.service
flask run
```

Open a new terminal to make predictions:

```sh
curl -d  '{"sepal length (cm)": 5.1, "sepal width (cm)": 3.5, "petal length (cm)": 1.4, "petal width (cm)": 0.2}' -H 'Content-Type: application/json' http://127.0.0.1:5000/

# with different values
curl -d  '{"sepal length (cm)": 5.9, "sepal width (cm)": 3.0, "petal length (cm)": 5.1, "petal width (cm)": 1.8}' -H 'Content-Type: application/json' http://127.0.0.1:5000/
```

Note: Ploomber exports a Python object that encapsulates the full inference pipeline (pre-processing + feature engineering + model inference), it can be deployed with any framework.

## Code

`src/ml_online`:

1. `pipeline-features.yaml`: feature engineering YAML spec
2. `pipeline.yaml`: training pipeline
3. `infer.py`: converts training pipeline to an inference pipeline
4. `service.py`: uses inference pipeline to serve predictions using flask

## Interactive console

Run in a terminal:

```sh
ploomber interact
```

Starts an interactive session with a `dag` variable, which is the
representation of the training pipeline, useful for debugging. Try the following:

```python
# get task names
list(dag)

# get task object
task = dag['get']

# get task information
task.source
task.product

# debug task
task.debug()

# enter "quit" to exit the debugger
```

## Testing

```sh
# run tests in the current environment
invoke test --inplace

# creates a new virtual environment before running tests - useful for setting up continuous integration
invoke test
```

## Deployment

This project is a Python package, you can generate a distribution archive (`tar.gz`) or a built distribution (`.whl`) for deployment:

```sh
python -m build
```

Files are saved in in the `dist/` directory. Both contain all the necesary pieces to serve predictions: dependencies, preprocessing code, and model file.

## Scale up training

If you want to train multiple models at once, you can export your training pipeline to run on Kubernetes/Argo or Airflow.

```sh
# install our package for exporting projects
pip install soopervisor

# export to kubernetes/argo
soopervisor export

# export to airflow
soopervisor export-airflow
```

Click here to go to Soopervisor's  [documentation](https://soopervisor.readthedocs.io/) or [Github](github.com/ploomber/soopervisor)