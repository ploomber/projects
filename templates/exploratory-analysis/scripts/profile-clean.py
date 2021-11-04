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

# Quick clean data profiling.


import pandas as pd
from pandas_profiling import ProfileReport

# + tags=["parameters"]
upstream = ['clean']
product = None
# -


df = pd.read_csv(upstream['clean']['data'])

ProfileReport(df, title="Clean Data Profiling Report")


