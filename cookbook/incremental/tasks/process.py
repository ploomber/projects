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

# %% tags=["parameters"]
upstream = ['load']
product = None

# %%
import pandas as pd

# %%
df = pd.read_csv(upstream['load']['data'], index_col='index')
df.head()

# %%
df_out = pd.DataFrame({'plus_one': df['x'] + 1})
df_out


# %%
df_out.to_csv(product['data'])

# %%
