from pathlib import Path

import pandas as pd


def serialize(value, product):
    Path(str(product)).parent.mkdir(parents=True, exist_ok=True)
    value.to_parquet(str(product))


def unserialize(product):
    return pd.read_parquet(str(product))
