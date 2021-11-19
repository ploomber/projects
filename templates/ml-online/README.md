<!-- start header -->
To run this example locally, [install Ploomber](https://ploomber.readthedocs.io/en/latest/get-started/install.html) and execute: `ploomber examples -n templates/ml-online`

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Ftemplates/ml-online%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=templates/ml-online%20issue)

Have questions? [Ask us anything on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/templates/ml-online/README.ipynb)
<!-- end header -->



<!-- #region -->
# Machine Learning pipeline with online API

<!-- start description -->
Load data, generate features, train a model, and deploy model with flask.
<!-- end description -->

Note: all commands must be executed in the `ml-online/` directory.

## Setup

```sh
pip install --editable ".[dev]"
```

## File layout

`src/ml_online`:

1. `pipeline-features.yaml`: feature engineering YAML spec
2. `pipeline.yaml`: training pipeline
3. `infer.py`: converts training pipeline to an inference pipeline
4. `service.py`: uses inference pipeline to serve predictions using Flask

## Training pipeline
<!-- #endregion -->

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

```python
from os import environ
import subprocess

def start_flask():
    """Start Flask and wait until it's ready
    """
    proc = subprocess.Popen(['flask', 'run'],
                        env=dict(environ, FLASK_APP='ml_online.service'),
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    
    while True:
        out = proc.stdout.readline()
        print(out.decode().strip())
    
        if b'5000' in out:
            break
    
    return proc
```

```python
proc = start_flask()
```

<!-- #region -->
*Note:* `start_flask()` is the same as executing the following a terminal:

```sh
export FLASK_APP=ml_online.service
flask run
```
<!-- #endregion -->

Open a new terminal to make predictions:

```python
import requests
```

```python
def make_request(data):
    """Hit the prediction endpoint
    """
    response = requests.post('http://127.0.0.1:5000/',
                             data=data,
                             headers={'Content-Type': 'application/json'})
    return response.json()
```

```python
make_request('{"sepal length (cm)": 5.1, "sepal width (cm)": 3.5, "petal length (cm)": 1.4, "petal width (cm)": 0.2}')
```

<!-- #region -->
*Note: The previous command is equivalent to running the following on the terminal*

```sh
curl -d  '{"sepal length (cm)": 5.1, "sepal width (cm)": 3.5, "petal length (cm)": 1.4, "petal width (cm)": 0.2}' -H 'Content-Type: application/json' http://127.0.0.1:5000/
```
<!-- #endregion -->

```python
make_request('{"sepal length (cm)": 5.9, "sepal width (cm)": 3.0, "petal length (cm)": 5.1, "petal width (cm)": 1.8}')
```

<!-- #region -->
*Note: The previous command is equivalent to running the following on the terminal*

```sh
curl -d  '{"sepal length (cm)": 5.9, "sepal width (cm)": 3.0, "petal length (cm)": 5.1, "petal width (cm)": 1.8}' -H 'Content-Type: application/json' http://127.0.0.1:5000/
```
<!-- #endregion -->

Note: Ploomber exports a Python object that encapsulates the entire inference pipeline (pre-processing + feature engineering + model inference). You can deploy it with any framework.

```python
# terminate flask app
proc.kill()
```

## Testing

The example contains some basic unit tests. To run them:

```sh
pytest -p no:warnings
```

<!-- #region -->

## Packaging

This project is a Python package. You can generate a distribution archive (`tar.gz`) or a built distribution (`.whl`) for deployment:


```sh
python -m build
```

<!-- #endregion -->

The previous command creates a `.whl` and a `.tar.gz` file in the `dist/` directory; both contain all the necessary pieces to serve predictions: dependencies, pre-processing code, and model file.