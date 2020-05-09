import pandas as pd
import seaborn as sns

# + tags=['parameters']
product = None
upstream = None

# +
df = pd.read_csv(upstream['clean.py']['data'])

df

sns.distplot(df.x)
