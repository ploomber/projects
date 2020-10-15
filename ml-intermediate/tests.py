import pandas as pd


def no_missing_values(product):
    df = pd.read_parquet(str(product))
    assert not df.isna().sum().sum(), f'Found missing values in {product}'
