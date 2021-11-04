# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# Get penguins data.


import seaborn as sns

# + tags=["parameters"]
upstream = None
product = None
# -


df = sns.load_dataset('penguins')

df.to_csv(product['data'], index=False)
