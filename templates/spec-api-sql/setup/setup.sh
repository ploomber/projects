set -e

pip install sqlalchemy faker numpy pandas
python simulate_data.py
mkdir -p ../output/
mv data.db ../data.db