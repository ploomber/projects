import pandas as pd
from sklearn import datasets


def get():
    """Get training data
    """
    d = datasets.load_iris()
    df = pd.DataFrame(d['data'])
    df.columns = d['feature_names']
    df['target'] = d['target']
    return df
