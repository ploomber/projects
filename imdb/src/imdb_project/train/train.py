from dstools import Env
from sklearn.linear_model import LogisticRegression
import pandas as pd
import psycopg2

env = Env()

con = psycopg2.connect(env.db.postgres)
df = pd.read_sql('select * from dataset', con=con)
con.close()

X = df.drop('label', axis=1).values
y = df.label.values

model = LogisticRegression()
model.fit(X, y)
