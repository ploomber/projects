import json

import pytest

from ml_online import service


@pytest.fixture
def client():
    service.app.config['TESTING'] = True

    with service.app.test_client() as client:
        yield client


def test_predict(client):
    rv = client.post('/',
                     data=json.dumps({
                         'sepal length (cm)': 5.1,
                         'sepal width (cm)': 3.5,
                         'petal length (cm)': 1.4,
                         'petal width (cm)': 0.2,
                     }),
                     content_type='application/json')
    assert b'{"prediction":0}\n' == rv.data
