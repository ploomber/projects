from flask import Flask, request, jsonify
import pandas as pd

from ml_online.infer import InferencePipeline

pipeline = InferencePipeline()
app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    """
    >>> export FLASK_APP=web.py
    >>> flask run
    >>> curl -d  '{"sepal length (cm)": 5.1, "sepal width (cm)": 3.5, "petal length (cm)": 1.4, "petal width (cm)": 0.2}' -H 'Content-Type: application/json' http://127.0.0.1:5000/
    """
    request_data = request.get_json()
    get = pd.DataFrame(request_data, index=[0])
    out = pipeline.predict(get=get)
    return jsonify({'prediction': int(out['terminal'])})
