import pandas as pd
import seaborn as sns

# + tags=["parameters"]

# -

df = pd.read_csv(upstream['posts-dump'])

df

sns.distplot(df.length)


