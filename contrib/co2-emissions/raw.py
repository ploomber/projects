from pathlib import Path
import zipfile
import urllib.request

# + tags=["parameters"]
upstream = None
product = {
    'nb': 'output/raw.ipynb',
    'zipped': 'output/raw.zip',
    'data': 'output/raw.csv'
}
# -

url = 'http://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.PC?downloadformat=csv'
urllib.request.urlretrieve(url, product['zipped'])

with zipfile.ZipFile(product['zipped'], 'r') as zip_ref:
    # the filename changes when they upload a new version...
    names = [name for name in zip_ref.namelist() if name.startswith('API')]
    assert len(names) == 1, 'Unknown list of files, update file to unzip...'
    raw_data = zip_ref.read(names[0])

Path(product['data']).write_bytes(raw_data)
