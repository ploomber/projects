"""
Tasks for the serving pipeline
"""
from pathlib import Path
import pickle

import pandas as pd
from sklearn import datasets


def get(product, sample):
    """Get input data to make predictions
    """
    Path(str(product)).parent.mkdir(parents=True, exist_ok=True)

    d = datasets.load_iris()

    df = pd.DataFrame(d['data'])
    df.columns = d['feature_names']

    if sample:
        df = df.sample(frac=0.1)

    df.to_parquet(str(product))


def predict(upstream, product, path_to_model):
    """Make predictions
    """
    df = pd.read_parquet(str(upstream['join']))

    with open(path_to_model, 'rb') as f:
        model = pickle.load(f)

    preds = model.predict(df)

    pd.DataFrame({'preds': preds}).to_csv(str(product))
