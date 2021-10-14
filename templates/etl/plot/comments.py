import pandas as pd
import seaborn as sns

# + tags=["parameters"]

# -

df = pd.read_csv(upstream['comments-dump'])

sns.distplot(df['count'])
