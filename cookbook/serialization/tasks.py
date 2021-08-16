import pandas as pd


def one_product():
    return 'my text output'


def many_products(upstream):
    text = upstream['one_product']
    df = pd.DataFrame({'x': range(10)})
    return {'something': df, 'another': f'{text} with more text'}


def joblib_product(upstream):
    up = upstream['many_products']
    df = up['something']

    return df['x'].values


def final_product(upstream):
    x = upstream['joblib_product']
    df = pd.DataFrame({'x': x})
    df['y'] = df['x'] + 1
    return df
