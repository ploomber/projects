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
import pandas as pd

# %% tags=["parameters"]
upstream = ['dump-table']
product = None

# %%
df = pd.read_parquet(upstream['dump-table'])

# %%
# most popular names
df.set_index('name').sort_values(by='number').tail(10).plot(kind='bar')

# %%
