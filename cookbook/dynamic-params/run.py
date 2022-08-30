# %%
"""
Run the pipeline with: python run.py
"""
from datetime import datetime
from glob import glob
from pathlib import Path
from ploomber.spec import DAGSpec


# %%
def run_number():
    """Returns an increasing integer
    """
    if not Path('products').exists():
        return 0

    return max([int(Path(path).name) for path in glob('products/*')]) + 1


# %%
def now():
    """Returns a string with the current timestamp
    """
    return str(datetime.now())


# %%
if __name__ == '__main__':
    # try switching run_number() with now()
    dag = DAGSpec('pipeline.yaml', env={'run_number': run_number()}).to_dag()
    dag.build()
