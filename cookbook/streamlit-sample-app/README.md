<!-- start header -->
To run this example locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/install.html) and execute: `ploomber examples -n cookbook/streamlit-sample-app`

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fcookbook/streamlit-sample-app%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=cookbook/streamlit-sample-app%20issue)

Have questions? [Ask us anything on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/cookbook/streamlit-sample-app/README.ipynb)
<!-- end header -->



# Streamlit sample integration

<!-- start description -->
Sample pipeline to profile penguins data, raw and clean.
Once the pipeline is ready you can launch the streamlit application to 
visualize the results.
<!-- end description -->

It contains two tasks, get and clean the data:

<!-- #md -->
```yaml
# Content of pipeline.yaml
tasks:
  - source: scripts/get.py
    product:
      nb: products/get.html
      data: products/raw.csv

  - source: scripts/clean.py
    product:
      nb: products/clean.html
      data: products/clean.csv

```
<!-- #endmd -->

Generate the plot (note that this requires `pygraphviz`, you can skip this if you want):

<!-- #md -->
```sh
ploomber plot
```
<!-- #endmd -->


Open the `pipeline.png` file to see the diagram.

## Build pipeline

```sh
ploomber build
```

Each task generates a CSV data file, go to the `products/` directory after
building the pipeline to see them.

Now we'll run the webapp (it takes ~1 minute)
```sh
# streamlit run st_app.py
```

Once it's done, it'll load the reports into the localhost and you can view your dashboard.