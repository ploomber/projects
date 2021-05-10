"""
Get data
"""
import seaborn as sns

# + tags=["parameters"]
upstream = None
product = None
# -

# +
df = sns.load_dataset('iris')
df.columns = [
    'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'
]
df.head()
# -

# +
df.to_csv(str(product['data']), index=False)
# -
