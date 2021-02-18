import pandas as pd
from sklearn import datasets


def get(sample):
    """Get training data
    """
    d = datasets.load_iris()
    df = pd.DataFrame(d['data'])

    if sample:
        df.sample(n=5)

    df.columns = d['feature_names']
    df['target'] = d['target']
    return df
