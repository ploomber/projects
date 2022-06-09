# %% tags=["parameters"]
upstream = ['1-get']
product = None


# %%
import pandas as pd
import seaborn as sns

# %%
# Loading raw data
print(upstream['1-get']['data'])
df = pd.read_csv(upstream['1-get']['data'])

# %%
# Profiling
sns.displot(df['state'])

# %%
sns.relplot(x="cases", y="deaths", data=df);

# %%
sns.relplot(x="cases", y="date", data=df);