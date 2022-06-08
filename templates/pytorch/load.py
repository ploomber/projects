# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
from utils import load_data

# %% tags=["parameters"]
upstream = None
# This is a placeholder, leave it as None
product = None


# %%
_ = load_data(product['raw'])
