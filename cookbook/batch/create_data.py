"""
Adds a new file to the input folder:

input/data-0.csv, input/data-1.csv, input/data-2.csv, etc.
"""
import os
from pathlib import Path

if __name__ == '__main__':
    Path('input').mkdir(exist_ok=True)
    n = len(os.listdir('input'))
    path = Path('input', f'data-{n}.csv')
    print(f'Saving {path!s}')
    path.write_text("""\
column, another_column
value, another_value
""")