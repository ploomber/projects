import pandas as pd
import seaborn as sns

# + tags=["parameters"]
product = None
upstream = {'join_dump.sql': None}

# +
df = pd.read_csv(str(upstream['join_dump.sql']))

sns.distplot(df.revenue)
