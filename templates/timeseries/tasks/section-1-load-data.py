# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
# ---

# %% tags=["soorgeon-imports"]
import statsmodels.api as sm
import matplotlib.pyplot as plt
from pathlib import Path
import pickle

# %% tags=["parameters"]
upstream = None
product = None

# %% [markdown]
# # ARIMA in Python 3

# %% [markdown]
# Based on https://github.com/williewheeler/time-series-demos/blob/master/arima/arima-python.ipynb.

# %%







plt.style.use('fivethirtyeight')

# %% [markdown] tags=[]
# ## 1 Load data

# %%
data = sm.datasets.co2.load_pandas()
y = data.data

# %% tags=["soorgeon-pickle"]
Path(product['y']).parent.mkdir(exist_ok=True, parents=True)
Path(product['y']).write_bytes(pickle.dumps(y))
