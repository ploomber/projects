<!-- start header -->
To run this locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n templates/spec-api-r`


Questions? [Ask us on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/templates/spec-api-r/README.ipynb)
<!-- end header -->



# R pipeline

<!-- start description -->
Load, clean and plot data with R.
<!-- end description -->

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
