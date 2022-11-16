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
upstream = None
product = None

# %%
import json
from pathlib import Path
import sqlite3

import pandas as pd

# %%
con = sqlite3.connect(path_to_db)

# %%
print(f'Loading since index: {index}')
df = pd.read_sql('SELECT * FROM numbers WHERE "index" > :index',
                 con=con,
                 params={'index': index},
                 index_col='index')

# %%
df.to_csv(product['data'])
