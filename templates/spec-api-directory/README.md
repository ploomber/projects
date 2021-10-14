<!-- start header -->
To run this example locally, execute: `ploomber examples -n spec-api-directory`.

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fspec-api-directory%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=spec-api-directory%20issue)

Have questions? [Ask us anything on Slack.](http://community.ploomber.io/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/spec-api-directory/README.ipynb)
<!-- end header -->



# Pipeline from directory

Pipeline from a directory of scripts.

## Build

```bash
mkdir output
ploomber build --entry-point '*.py'
```

Output stored in the `output/` directory.


## Describe

This pipeline contains five steps. The last task trains a model and outputs a
report and a model file. To get the pipeline description:

```bash
ploomber status --entry-point '*.py'
```

`--entry-point '*.py'` means "all files with py extension are tasks in the
pipeline". If all the files in the current directory are tasks, you can also
use the shortcut `--entry-point .`.