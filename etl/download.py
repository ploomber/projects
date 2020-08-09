# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---
from pathlib import Path
import urllib

from pyunpack import Archive

# + tags=["parameters"]
upstream = None
product = None

# +
url = 'https://archive.org/download/stackexchange/arduino.stackexchange.com.7z'
urllib.request.urlretrieve(url, product['zipped'])

Path(product['extracted']).mkdir(exist_ok=True)
Archive(product['zipped']).extractall(product['extracted'])
