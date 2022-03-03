# %% tags=["parameters"]
upstream = ['3-clean']
product = None


# %%
import pandas as pd
import seaborn as sns

# %%
# Loading raw data
print(upstream['3-clean']['data'])
df = pd.read_parquet(upstream['3-clean']['data'])

# %%
# Profiling
sns.displot(df['state'])

# %%
sns.relplot(x="confirmed_cases", y="confirmed_deaths", data=df);

# %%
sns.relplot(x="confirmed_cases", y="date", data=df);