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

# Clean penguins data.


import pandas as pd

# + tags=["parameters"]
upstream = ['get']
product = None
# -

df = pd.read_csv(upstream['get']['data'])

print(f'Raw data has {len(df)} rows...')

df.head()

# really simple cleaning, remove if the row has nas...
clean = df[df.isna().sum(axis=1) == 0]

print(f'Clean data has {len(clean)} rows...')

clean.to_csv(product['data'], index=False)
