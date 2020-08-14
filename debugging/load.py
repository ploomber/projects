import pandas as pd

# + tags=["parameters"]
upstream = None
product = {
    'nb': 'output/raw.ipynb',
    'train': 'output/train.csv',
    'test': 'output/test.csv'
}

# -

# +
X_train = pd.DataFrame({'cat': ['a', 'b', 'c']})
X_test = pd.DataFrame({'cat': ['a', 'b', 'd']})

# +
X_train.to_csv(product['train'], index=False)
X_test.to_csv(product['test'], index=False)
