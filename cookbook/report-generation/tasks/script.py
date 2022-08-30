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
import numpy as np

# %% tags=["parameters"]
upstream = None
# This is a placeholder, leave it as None
product = None


# %%
numbers = np.random.rand(100)
df = pd.DataFrame({'x': numbers})

# %% [markdown]
# ## Boxplot
#
# This is some descriptive text.

# %%
df.plot(kind='box')

# %% [markdown]
# ## Density plot
#
# This is some descriptive text.

# %%
df.plot(kind='density')
