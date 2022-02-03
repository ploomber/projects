# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# Get penguins data.


# %%
import seaborn as sns

# %% tags=["parameters"]
upstream = None
product = None


# %%
df = sns.load_dataset('penguins')

# %%
df.to_csv(product['data'], index=False)
