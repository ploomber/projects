# %%
"""
Visualize
"""
# this is an annotated script
import pandas as pd
import seaborn as sns

# %% tags=["parameters"]
upstream = ['3-clean']
product = None

# %%
df = pd.read_parquet(upstream['3-clean']['data'])

# %%
sns.displot(df.death_percents)

# %%
sns.displot(df.cases)

# %%
sns.displot(df.deaths)

# %%
df.head()
