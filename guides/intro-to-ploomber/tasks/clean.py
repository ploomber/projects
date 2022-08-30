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
import pandas as pd
from pathlib import Path
import pickle

# %% tags=["parameters"]
upstream = ['load']
product = None

# %% tags=["soorgeon-unpickle"]
data = pickle.loads(Path(upstream['load']['data']).read_bytes())

# %% [markdown]
# ## Clean

# %%
data['Cases'] = data['Cases'].str.replace(',', '')
data['Tests'] = data['Tests'].str.replace(',', '')

data['Cases'] = pd.to_numeric(data['Cases'])
data['Tests'] = pd.to_numeric(data['Tests'])

# print(data.info())
# data_numeric = data.select_dtypes(include=['float64', 'int64'])
# plt.figure(figsize=(20, 10))
# sns.pairplot(data_numeric)
# plt.show()

# %% tags=["soorgeon-pickle"]
Path(product['data']).parent.mkdir(exist_ok=True, parents=True)
Path(product['data']).write_bytes(pickle.dumps(data))
