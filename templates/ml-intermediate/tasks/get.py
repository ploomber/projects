from pathlib import Path
import pandas as pd
from sklearn import datasets


def fn(product, sample):
    """Get data
    """
    Path(str(product)).parent.mkdir(parents=True, exist_ok=True)

    d = datasets.load_iris()

    df = pd.DataFrame(d['data'])
    df.columns = d['feature_names']
    df['target'] = d['target']

    if sample:
        df = df.sample(frac=0.1)

    df.to_parquet(str(product))
