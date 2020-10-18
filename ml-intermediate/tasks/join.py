import pandas as pd


def fn(upstream, product):
    """Join raw data with generated features
    """
    first = pd.read_parquet(str(upstream['get']))
    second = pd.read_parquet(str(upstream['features']))
    df = first.join(second)
    df.to_parquet(str(product))
