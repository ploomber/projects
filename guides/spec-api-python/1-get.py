"""
Get data
"""
import seaborn as sns
from pathlib import Path

# + tags=["parameters"]
upstream = None
product = None
# -

df = sns.load_dataset('iris')
df.columns = [
    'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'
]
df.head()

# +
Path('output').mkdir(exist_ok=True)

df.to_csv(str(product['data']), index=False)
# -


