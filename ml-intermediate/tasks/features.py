from pathlib import Path
import pandas as pd


def sepal_area(upstream, product):
    """Compute sepal area
    """
    Path(str(product)).parent.mkdir(parents=True, exist_ok=True)

    data = pd.read_parquet(str(upstream['get']))
    ft = data['sepal length (cm)'] * data['sepal width (cm)']
    df = pd.DataFrame({'sepal area (cm2)': ft})
    df.to_parquet(str(product))


def petal_area(upstream, product):
    """Compute petal area
    """
    Path(str(product)).parent.mkdir(parents=True, exist_ok=True)

    data = pd.read_parquet(str(upstream['get']))
    ft = data['petal length (cm)'] * data['petal width (cm)']
    df = pd.DataFrame({'petal area (cm2)': ft})
    df.to_parquet(str(product))
