# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

# %% tags=["parameters"]
upstream = ['dump-table']
product = None

# %%
df = pd.read_parquet(upstream['dump-table'])

# %%
# most popular names
df.groupby('name').number.sum().sort_values().tail(10).plot(kind='bar')

# %%
