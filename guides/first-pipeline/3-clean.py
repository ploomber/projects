# %%
"""
Clean
"""
import pandas as pd

# %% tags=["parameters"]
upstream = ['1-get']
product = None

# %%
df = pd.read_csv(upstream['1-get']['data'])

# %%
df.head()

# %%
len(df.index)

# %%
# Clean data
df = df.dropna()
len(df.index)

# %%
# Adding columns
df['death_percents'] = df.deaths / df.cases * 100

# %%
# Save final df
df.to_parquet(str(product['data']), index=False)
