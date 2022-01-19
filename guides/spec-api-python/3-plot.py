"""
Visualize
"""
# this is an annotated script
import pandas as pd
import seaborn as sns

# + tags=["parameters"]
upstream = ['2-clean']
product = None
# -

df = pd.read_csv(upstream['2-clean']['data'])

sns.distplot(df.sepal_length)

sns.distplot(df.sepal_width)

df.head()
