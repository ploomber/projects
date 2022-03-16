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
upstream = ['section-4-modeling-hyperparameter-optimization-via-grid-search']
product = None

# %% tags=["soorgeon-unpickle"]
min_model = pickle.loads(Path(upstream['section-4-modeling-hyperparameter-optimization-via-grid-search']['min_model']).read_bytes())

# %% [markdown]
# ## 5 Model fit and diagnostics

# %% [markdown]
# We kept the best model from the HPO, so now we can explore it.

# %%
results = min_model # To align with the blog post
results.summary().tables[1]

# %%
# KDE = kernel density estimate
# Q-Q plot = quantile/quantile
results.plot_diagnostics(figsize=(15, 10))
plt.show()

# %% [markdown]
# References:
#
# - [Kernel density estimation](https://en.wikipedia.org/wiki/Kernel_density_estimation)
# - [Q-Q plot](https://en.wikipedia.org/wiki/Q%E2%80%93Q_plot)

# %% tags=["soorgeon-pickle"]
Path(product['results']).parent.mkdir(exist_ok=True, parents=True)
Path(product['results']).write_bytes(pickle.dumps(results))
