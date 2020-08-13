"""
This script just prepares data we need for the example, it's not part of the
pipeline
"""
import sqlite3
import numpy as np
import pandas as pd


def sample_in_range(a, b):
    return ((b - a) * np.random.random_sample(100) + a).astype(int)


df = pd.DataFrame({
    'score': sample_in_range(0, 10),
    'age': sample_in_range(21, 80)
})
df.loc[:10, 'score'] = np.nan
df.loc[11:20, 'age'] = -42

conn = sqlite3.connect('../output/data.db')
df.to_sql('my_table', con=conn)
