import pickle
from importlib import resources

from ploomber import OnlineDAG

import ml_online


class InferencePipeline(OnlineDAG):
    """Pipeline for online predictions

    Examples
    --------
    >>> from ml_online.infer import InferencePipeline
    >>> pipeline = InferencePipeline()
    >>> get = {"sepal length (cm)": 5.1, "sepal width (cm)": 3.5,
    ...        "petal length (cm)": 1.4, "petal width (cm)": 0.2}
    >>> pipeline.predict(get=get)
    """
    @staticmethod
    def get_partial():
        with resources.path(ml_online,
                            'pipeline-features.yaml') as path_to_spec:
            path = path_to_spec

        return path

    @staticmethod
    def terminal_params():
        model = pickle.loads(resources.read_binary(ml_online, 'model.pickle'))
        return dict(model=model)

    @staticmethod
    def terminal_task(upstream, model):
        return int(model.predict(upstream['features'])[0])
