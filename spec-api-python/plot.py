# this is an annotated script
import numpy as np
import pandas as pd
import seaborn as sns

# + tags=["parameters"]
upstream = ["clean"]
# outputs two files: the script itself as a notebook and a csv file
product = {"nb": "output/plot.ipynb"}
# -

df = pd.read_csv(upstream['clean']['data'])

sns.distplot(df.sepal_length)

sns.distplot(df.sepal_width)

df.head()
