# +
import json
from pathlib import Path

import pandas as pd
from ploomber.exceptions import DAGBuildEarlyStop

def check_if_new_records(product):
    df = pd.read_csv(product['data'])
    n_to_process = len(df)

    if not n_to_process:
        raise DAGBuildEarlyStop('No records to process, stopping execution.')

def store_index(task, path_to_index):
    df = pd.read_csv(task.upstream['process'].product['data'], index_col='index')

    # NOTE: this assumes the indexes are incremental
    index_latest_new = df.index.max()
    print(f'Storing index: {index_latest_new}')
    path = Path(path_to_index)
    path.write_text(json.dumps(dict(latest=int(index_latest_new))))
