from pathlib import Path
from sqlalchemy import create_engine
import numpy as np
import pandas as pd
from faker import Faker

n = 1000
n_products = 100
fake = Faker()

sales_data = {
    'country': [fake.country() for _ in range(n)],
    'purchase_date': [fake.date_between() for _ in range(n)],
    'product_id': np.random.randint(0, n_products, n),
}

prices_data = {
    'product_id': range(n_products),
    'price': 100 * np.random.random(n_products) + 50,
}

sales = pd.DataFrame(sales_data)
prices = pd.DataFrame(prices_data)

if Path('data.db').exists():
    Path('data.db').unlink()

if Path('../data.db').exists():
    Path('../data.db').unlink()

engine = create_engine('sqlite:///data.db')

sales.to_sql('sales', engine)
prices.to_sql('prices', engine)
