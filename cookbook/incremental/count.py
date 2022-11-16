import sqlite3

con = sqlite3.connect('data.db')

numbers_count = con.execute('SELECT COUNT(*) FROM numbers').fetchone()[0]
print(f'numbers has {numbers_count} rows')

try:
    plus_one = con.execute('SELECT COUNT(*) FROM plus_one').fetchone()[0]
except sqlite3.OperationalError:
    print('plus_one table does not exist')
else:
    print(f'plus_one has {plus_one} rows')
