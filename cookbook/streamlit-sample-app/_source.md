---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Streamlit sample integration

<!-- start description -->
Sample pipeline to profile penguins data, raw and clean.
Once the pipeline is ready you can launch the streamlit application to 
visualize the results.
<!-- end description -->

It contains two tasks, get and clean the data:

<% expand('pipeline.yaml') %>

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