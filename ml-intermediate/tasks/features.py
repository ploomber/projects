import pandas as pd
from .util import square


def fn(upstream, product):
    """Generate new features from existing columns
    """
    data = pd.read_parquet(str(upstream['get']))
    ft = square(data['sepal length (cm)'])
    df = pd.DataFrame({'sepal area (cm2)': ft})
    df.to_parquet(str(product))
