<!-- start header -->
To run this example locally, execute: `ploomber examples -n ml-advanced`.

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fml-advanced%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=ml-advanced%20issue)

Have questions? [Ask us anything on Slack.](http://community.ploomber.io/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/ml-advanced/README.ipynb)
<!-- end header -->



# ML advanced

ML pipeline using the Python API. Shows how to package project, test it using pytest, and train models in parallel.

## Build

```sh
ploomber build --entry-point ml_advanced.pipeline.make
```

## Testing

```bash
# complete (force execution of all tasks)
pytest --force
```

```bash
# incremental (will only run the tasks that have changed)
pytest
```