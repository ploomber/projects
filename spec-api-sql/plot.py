import pandas as pd
import seaborn as sns

# + tags=["parameters"]
product = None
upstream = {'join_dump'}


# +
df = pd.read_csv(str(upstream['join_dump']))
sns.distplot(df.revenue)



