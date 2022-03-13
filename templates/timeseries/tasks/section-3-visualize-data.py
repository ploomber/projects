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
import matplotlib.pyplot as plt
from pathlib import Path
import pickle

# %% tags=["parameters"]
upstream = ['section-2-preprocess-data']
product = None

# %% tags=["soorgeon-unpickle"]
y = pickle.loads(Path(upstream['section-2-preprocess-data']['y']).read_bytes())

# %% [markdown]
# ## 3 Visualize data

# %%
y.plot(figsize=(15, 6))
plt.show()
