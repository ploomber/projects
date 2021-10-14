"""
Visualize
"""
# this is an annotated script
import pandas as pd
import seaborn as sns

# + tags=["parameters"]
upstream = ["clean"]
product = None
# -

df = pd.read_csv(upstream['clean']['data'])

sns.distplot(df.sepal_length)

sns.distplot(df.sepal_width)

df.head()
