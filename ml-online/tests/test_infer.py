import pandas as pd
from ploomber.spec import DAGSpec

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


def test_no_training_serve_skew():
    """
    Test for training-serving skew (feature engineering in training and serving
    should be the same)
    """
    dag = DAGSpec.find().to_dag()

    # load raw data
    get = pd.read_parquet(dag['get'].product)
    del get['target']

    # load feature vectors
    join = pd.read_parquet(dag['join'].product)
    del join['target']

    pipeline = InferencePipeline()

    # make predictions using the online pipeline (if training set is large
    # you can take a random sample)
    online = [
        pipeline.predict(get=get.loc[[idx]])['join'] for idx in join.index
    ]

    # cast to a data frame
    online_df = pd.concat(online)
    online_df.index = join.index

    # compare data frames
    assert online_df.equals(join)
