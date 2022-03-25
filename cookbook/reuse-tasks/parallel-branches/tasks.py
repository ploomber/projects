import pandas as pd
from sklearn.datasets import load_iris


def make_train(product):
    df = load_iris(as_frame=True)['data']
    df[:100].to_csv(product, index=False)


def make_test(product):
    df = load_iris(as_frame=True)['data']
    df[100:].to_csv(product, index=False)


def drop_columns(upstream, product):
    keys = list(upstream)
    df = pd.read_csv(upstream[keys[0]])
    df.to_csv(product, index=False)


def clean(upstream, product):
    keys = list(upstream)
    df = pd.read_csv(upstream[keys[0]])
    df.to_csv(product, index=False)