<!-- start header -->
To run this example locally, execute: `ploomber examples -n spec-api-r`.

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fspec-api-r%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=spec-api-r%20issue)

Have questions? [Ask us anything on Slack.](http://community.ploomber.io/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/spec-api-r/README.ipynb)
<!-- end header -->



# R pipeline

R pipeline.

**Note:** If using conda (`environment.yml`), R will be installed and configured. If using pip (`requirements.txt`), you must install R and [configure it yourself]( https://github.com/IRkernel/IRkernel).


## Pipeline description

This pipeline contains three tasks. The last task generates a plot. To get the
pipeline description:

```bash
ploomber status
```

## Build the pipeline from the command line

```bash
mkdir output
ploomber build
```

Output stored in the ``output/`` directory.