"""
Get data
"""
import pandas as pd

# + tags=["parameters"]
upstream = None
product = None
# -

# +
df = pd.read_csv('https://archive.ics.uci.edu'
                 '/ml/machine-learning-databases'
                 '/iris/iris.data')
df.columns = [
    'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'
]
df.head()
# -

# +
df.to_csv(str(product['data']), index=False)
# -
