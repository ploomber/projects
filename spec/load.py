from pathlib import Path
import pandas as pd
import numpy as np

# + tags=["parameters"]
product = None
upstream = None

# +
Path('output').mkdir(exist_ok=True)
data = np.random.rand(1000, 10)
df = pd.DataFrame(data)
df.to_csv(str(product['data']), index=False)
