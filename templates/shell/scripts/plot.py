# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + tags=["parameters"]
upstream = ['download']
# This is a placeholder
product = None

# +
import pandas as pd
import seaborn as sns

df = pd.read_csv(upstream['download'])

sns.histplot(df.body_mass_g)
