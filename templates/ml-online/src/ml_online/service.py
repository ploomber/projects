from flask import Flask, request, jsonify
import pandas as pd

from ml_online.infer import InferencePipeline

pipeline = InferencePipeline()
app = Flask(__name__)


@app.route('/', methods=['POST'])
def predict():
    request_data = request.get_json()
    get = pd.DataFrame(request_data, index=[0])
    out = pipeline.predict(get=get)
    return jsonify({'prediction': int(out['terminal'])})
