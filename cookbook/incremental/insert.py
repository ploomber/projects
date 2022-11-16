import sqlite3

import pandas as pd
import numpy as np

print('Appending 100 records...')

con = sqlite3.connect('data.db')
df = pd.DataFrame({'x': np.random.rand(100)})

try:
    count = con.execute('SELECT COUNT(*) FROM numbers').fetchone()[0]
except sqlite3.OperationalError:
    count = 0

lower = count + 1
upper = lower + 100
df.index = np.arange(lower, upper)
print(f'Index range: {df.index.min()}, {df.index.max()}')

df.to_sql(name='numbers', con=con, if_exists='append')

print('Done.')
