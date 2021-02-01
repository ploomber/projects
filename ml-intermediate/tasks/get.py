from pathlib import Path
import pandas as pd
from sklearn import datasets


def fn(product, sample):
    """Get data
    """
    # make parent dir exists
    Path(str(product)).parent.mkdir(parents=True, exist_ok=True)

    d = datasets.load_iris()

    df = pd.DataFrame(d['data'])
    df.columns = d['feature_names']
    df['target'] = d['target']
    # for the purpose of this example, let's replicate this data frame to show
    # the benefit of sampling
    df = pd.concat([df] * 5000, ignore_index=True)

    if sample:
        print('Sampling 10%')
        df = df.sample(frac=0.1)
    else:
        print('Using the full dataset')

    df.to_parquet(str(product))
