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
upstream = ['download']
# This is a placeholder
product = None

# %%
import pandas as pd
import seaborn as sns

df = pd.read_csv(upstream['download'])

sns.histplot(df.body_mass_g)
