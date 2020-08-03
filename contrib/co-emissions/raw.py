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

# +
url = 'http://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.PC?downloadformat=csv'
urllib.request.urlretrieve(url, product['zipped'])

with zipfile.ZipFile(product['zipped'], 'r') as zip_ref:
    raw_data = zip_ref.read('API_EN.ATM.CO2E.PC_DS2_en_csv_v2_1217665.csv')

Path(product['data']).write_bytes(raw_data)
