set -e

pip install sqlalchemy faker
python simulate_data.py
mkdir output/