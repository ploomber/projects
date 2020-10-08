set -e

pip install sqlalchemy faker numpy pandas
python simulate_data.py
mkdir ../output/
mv data.db ../data.db