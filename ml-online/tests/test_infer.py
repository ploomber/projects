import pytest
import pandas as pd

from ml_online.infer import InferencePipeline


def test_predict():
    mapping = {
        'sepal length (cm)': 5.1,
        'sepal width (cm)': 3.5,
        'petal length (cm)': 1.4,
        'petal width (cm)': 0.2,
    }
    pipeline = InferencePipeline()
    get = pd.DataFrame(mapping, index=[0])
    assert pipeline.predict(get=get)['terminal'] is not None
