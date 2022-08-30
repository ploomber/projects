# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import mlflow

# %% tags=["parameters"]
upstream = ['fit-*']
product = None
mlflow_tracking_uri = None

# %%
mlflow.set_tracking_uri(mlflow_tracking_uri)

# %%
runs = mlflow.search_runs(experiment_ids=['1', '2'],
                          max_results=1,
                          order_by=['metrics.accuracy'])

# %%
runs.T
