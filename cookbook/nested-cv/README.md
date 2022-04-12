<!-- start header -->
To run this example locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/install.html) and execute: `ploomber examples -n cookbook/nested-cv`

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fcookbook/nested-cv%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=cookbook/nested-cv%20issue)

Have questions? [Ask us anything on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/cookbook/nested-cv/README.ipynb)
<!-- end header -->



# Nested cross-validation

<!-- start description -->
Nested cross-validation for model selection and hyperparameter tuning.
<!-- end description -->

More details in our [blog.](https://ploomber.io/blog/nested-cv/)

<!-- #md -->
```yaml
# Content of pipeline.yaml
executor: parallel

tasks:
  - source: tasks/load.py
    product:
      nb: products/load.html
      data: products/data.csv

  - source: tasks/fit.py
    name: fit-
    product:
      nb: products/fit.html
      model: products/model.pkl
    grid:
      - model: sklearn.ensemble.RandomForestClassifier
        model_params:
          # optimize over these parameters
          - n_estimators: [2, 5]
            criterion: [gini, entropy]
    
      - model: sklearn.svm.SVC
        model_params:
          # optimize over these parameters
          - kernel: [linear, poly]
            C: [0.1, 1.0]
      
      

```
<!-- #endmd -->

Plot:

```sh
# run this in a terminal
ploomber plot
```

```python
# run this in a python session
from IPython.display import Image
Image('pipeline.png')
```

Run the pipeline:

```sh
# run this in a terminal
ploomber build
```