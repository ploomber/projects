import pandas as pd


def fn(upstream, product):
    """Join raw data with generated features
    """
    first = pd.read_parquet(str(upstream['get']))
    sepal = pd.read_parquet(str(upstream['sepal_area']))
    petal = pd.read_parquet(str(upstream['petal_area']))
    df = first.join(sepal).join(petal)
    df.to_parquet(str(product))
