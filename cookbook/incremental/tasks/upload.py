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
upstream = ['process']
product = None

# %%
import sqlite3

import pandas as pd

# %%
df = pd.read_csv(upstream['process']['data'], index_col='index')
df

# %%
con = sqlite3.connect(path_to_db)

# %%
df.to_sql(name='plus_one', con=con, if_exists='append')
