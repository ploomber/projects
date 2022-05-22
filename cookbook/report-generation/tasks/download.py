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

# %% tags=["parameters"]
upstream = None
product = None


# %% [markdown]
# # Some title
#
# Some text.

# %%
from pathlib import Path

# %%
Path(product['data']).touch()
