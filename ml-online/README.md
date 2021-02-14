# Online API

Requires [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

## Setup development environment

```sh
pip installl invoke

# install dependencies
invoke setup

# activate environment
conda activate ml-online
```

## Testing

```sh
# creates a fresh virtual environment before running tests
invoke test

# ...or to run tests in the current environment
invoke test --inplace
```

## Running the training pipeline

```sh
ploomber build
```

## Interactive console (for debugging)

```
ploomber interact
```

## Online API

Start service:

```sh
export FLASK_APP=ml_online.service
flask run
```

In a new terminal:

```sh
curl -d  '{"sepal length (cm)": 5.1, "sepal width (cm)": 3.5, "petal length (cm)": 1.4, "petal width (cm)": 0.2}' -H 'Content-Type: application/json' http://127.0.0.1:5000/

# with different values
curl -d  '{"sepal length (cm)": 5.9, "sepal width (cm)": 3.0, "petal length (cm)": 5.1, "petal width (cm)": 1.8}' -H 'Content-Type: application/json' http://127.0.0.1:5000/
```


## Releasing models

[TO DO]

## Exporting to Kubernetes (via Argo) or Airflow (for large-scale training)

If you want to export to Airflow or Kubernetes, add "soopervisor" to your
dependencies and check out the [docs](https://soopervisor.readthedocs.io/).

```sh
# export to kubernetes/argo
soopervisor export

# export to airflow
soopervisor export-airflow
```
