import pandas as pd


def sepal_area(upstream):
    """Compute sepal area
    """
    data = upstream['get']
    ft = data['sepal length (cm)'] * data['sepal width (cm)']
    df = pd.DataFrame({'sepal area (cm2)': ft})
    return df


def petal_area(upstream):
    """Compute petal area
    """
    data = upstream['get']
    ft = data['petal length (cm)'] * data['petal width (cm)']
    df = pd.DataFrame({'petal area (cm2)': ft})
    return df


def join(upstream):
    """Join raw data with generated features
    """
    first = upstream['get']
    sepal = upstream['sepal_area']
    petal = upstream['petal_area']
    df = first.join(sepal).join(petal)

    # make sure features are always generated in the same order
    df = df[sorted(df.columns)]

    return df
