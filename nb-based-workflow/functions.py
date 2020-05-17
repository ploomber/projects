import pandas as pd
import numpy as np


def load(product):
    df = pd.DataFrame({'x': np.random.rand(500)})
    df.to_csv(str(product), index=False)
