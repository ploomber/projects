from pathlib import Path
import pandas as pd
from sklearn import datasets


def get(product, sample):
    """Get data
    """
    # make parent dir exists
    Path(str(product)).parent.mkdir(parents=True, exist_ok=True)

    d = datasets.load_iris()
    df = pd.DataFrame(d['data'])
    df.columns = d['feature_names']
    df['target'] = d['target']

    if sample:
        print('Sampling 10%')
        df = df.sample(frac=0.1)
    else:
        print('Using the full dataset')

    df.to_parquet(str(product))


def features(upstream, product):
    """Generate new features from existing columns
    """
    data = pd.read_parquet(str(upstream['get']))
    ft = data['sepal length (cm)'] * data['sepal width (cm)']
    df = pd.DataFrame({'sepal area (cm2)': ft})
    df.to_parquet(str(product))


def join(upstream, product):
    """Join raw data with generated features
    """
    a = pd.read_parquet(str(upstream['get']))
    b = pd.read_parquet(str(upstream['features']))
    df = a.join(b)
    df.to_parquet(str(product))
