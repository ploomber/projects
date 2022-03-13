# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
# ---

# %% tags=["soorgeon-imports"]

from pathlib import Path
import pickle

# %% tags=["parameters"]
upstream = ['section-1-load-data']
product = None

# %% tags=["soorgeon-unpickle"]
y = pickle.loads(Path(upstream['section-1-load-data']['y']).read_bytes())

# %% [markdown]
# ## 2 Preprocess data

# %%
# The 'MS' string groups the data into buckets by the start of the month
y = y['co2'].resample('MS').mean()

# 'bfill' means that we use the value before filling in missing values
y = y.fillna(y.bfill())

y

# %% tags=["soorgeon-pickle"]
Path(product['y']).parent.mkdir(exist_ok=True, parents=True)
Path(product['y']).write_bytes(pickle.dumps(y))
