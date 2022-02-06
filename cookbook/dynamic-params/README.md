<!-- start header -->
To run this example locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/install.html) and execute: `ploomber examples -n cookbook/dynamic-params`

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fcookbook/dynamic-params%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=cookbook/dynamic-params%20issue)

Have questions? [Ask us anything on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/cookbook/dynamic-params/README.ipynb)
<!-- end header -->



# Dynamic params

<!-- start description -->
Pipeline parameters whose values are computed at runtime.
<!-- end description -->

Run the pipeline:

```sh
python run.py
```

Check output (stored in directory with name `0`):

```sh
ls products
```

Run again:

```sh
python run.py
```

Check output (this time, stored in directory with name `1`):

```sh
ls products
```