import pandas as pd


def sepal(product, upstream):
    """Compute sepal area
    """
    data = pd.read_csv(upstream['get'])
    ft = data['sepal length (cm)'] * data['sepal width (cm)']
    df = pd.DataFrame({'sepal area (cm2)': ft})
    df.to_csv(product, index=False)


def petal(product, upstream):
    """Compute petal area
    """
    data = pd.read_csv(upstream['get'])
    ft = data['petal length (cm)'] * data['petal width (cm)']
    df = pd.DataFrame({'petal area (cm2)': ft})
    df.to_csv(product, index=False)


def features(product, upstream):
    """Join raw data with generated features
    """
    first = pd.read_csv(upstream['get'])
    sepal = pd.read_csv(upstream['sepal'])
    petal = pd.read_csv(upstream['petal'])
    df = first.join(sepal).join(petal)
    df = df[sorted(df.columns)]
    df.to_csv(product, index=False)
