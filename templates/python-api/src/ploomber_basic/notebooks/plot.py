import pandas as pd
import seaborn as sns

# + tags=["parameters"]
product = None
upstream = None

# +
df = pd.read_csv(upstream['clean']['data'])

# +
df['x'] = df['x'] + 1

# +
sns.distplot(df.x)
