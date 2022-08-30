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
upstream = ['load']
product = None


# %%
df = pd.read_csv(upstream['load']['data']).set_index('name')

# %%
df

# %%
df.plot(kind='barh')
