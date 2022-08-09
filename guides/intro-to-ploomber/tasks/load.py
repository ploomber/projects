# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% tags=["soorgeon-imports"]
import pandas as pd
import warnings
from pathlib import Path
import pickle

# %% tags=["parameters"]
upstream = None
product = None

# %% tags=["injected-parameters"]
# This cell was injected automatically based on your stated upstream dependencies (cell above) and pipeline.yaml preferences. It is temporary and will be removed when you save this notebook
product = {
    "data": "/home/jovyan/onboarding/output/load-data.pkl",
    "nb": "/home/jovyan/onboarding/output/load.ipynb",
}


# %% [markdown] tags=[]
# # Covid cases & Testing Regression
#
# ## Load

# %% tags=[]
# noqa
warnings.filterwarnings('ignore')
data = pd.read_csv("https://raw.githubusercontent.com/Ayushijain09/Regression-on-COVID-dataset/master/COVID-19_Daily_Testing.csv")
data.head()

# %% tags=["soorgeon-pickle"]
Path(product['data']).parent.mkdir(exist_ok=True, parents=True)
Path(product['data']).write_bytes(pickle.dumps(data))
