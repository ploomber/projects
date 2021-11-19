<!-- start header -->
To run this example locally, [install Ploomber](https://ploomber.readthedocs.io/en/latest/get-started/install.html) and execute: `ploomber examples -n cookbook/grid`

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fcookbook/grid%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=cookbook/grid%20issue)

Have questions? [Ask us anything on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/cookbook/grid/README.ipynb)
<!-- end header -->



# Task grids

<!-- start description -->
An example showing how to create a grid of tasks to train models with different parameters.
<!-- end description -->

<!-- #md -->
```yaml
# Content of pipeline.yaml
  - source: scripts/fit.py
    # generates tasks fit-1, fit-2, etc
    name: fit-
    # disabling static_analysis because the notebook does not have
    # a fixed set of parameters (depends on random-forest vs ada-boost)
    static_analysis: False
    product:
      nb: products/report.html
      model: products/model.pickle
    grid:
      # generates 6 tasks (1 * 3 * 2)
      - model_type: [random-forest]
        n_estimators: [1, 3, 5]
        criterion: [gini, entropy]

      # generates 9 tasks (1 * 3 * 2)
      - model_type: [ada-boost]
        n_estimators: [1, 3, 5]
        learning_rate: [1, 2]
```
<!-- #endmd -->

Run the pipeline:

```sh
ploomber build
```