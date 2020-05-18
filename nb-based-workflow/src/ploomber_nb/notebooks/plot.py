# + tags=[]
import pandas as pd
import seaborn as sns

# + tags=["parameters"]
product = None
upstream = None

# + tags=[]
df = pd.read_csv(upstream['clean.py']['data'])

df['x'] = df['x'] + 1
# -

sns.distplot(df.x)


