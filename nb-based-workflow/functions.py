import pandas as pd
import numpy as np


def load(product):
    df = pd.DataFrame({'x': np.random.rand(500)})
    df['x'] = df['x'] + 1
    df.to_csv(str(product), index=False)
