import pandas as pd
from sklearn import datasets


def get(product):
    d = datasets.load_iris()
    df = pd.DataFrame(d['data'])

    df.columns = d['feature_names']
    df['target'] = d['target']
    df.to_csv(product, index=False)
