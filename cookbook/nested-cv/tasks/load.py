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

# %%
from sklearn.datasets import load_iris

# %% tags=["parameters"]
upstream = None
product = None


# %% tags=["injected-parameters"]
# This cell was injected automatically based on your stated upstream dependencies (cell above) and pipeline.yaml preferences. It is temporary and will be removed when you save this notebook
product = {
    "nb": "/Users/Edu/dev/docs/drafts/0-nested-cross-val/nested-cv/products/load.html",
    "data": "/Users/Edu/dev/docs/drafts/0-nested-cross-val/nested-cv/data.csv",
}


# %% tags=[]
iris = load_iris(as_frame=True)

# %%
iris['frame'].to_csv(product['data'], index=False)

# %%
