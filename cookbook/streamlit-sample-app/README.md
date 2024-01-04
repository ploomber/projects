<!-- start header -->
To run this locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n cookbook/streamlit-sample-app`

Questions? [Ask us on Slack.](https://ploomber.io/community/)

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
