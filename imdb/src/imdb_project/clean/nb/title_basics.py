# +
from imdb_project import pipeline

import pandas as pd
# -

dag = pipeline.make()

df = pd.read_parquet(str(dag['clean_title_basics']))

df.head()


