import time
from pathlib import Path
from glob import glob

from ploomber.spec import DAGSpec


def run():
    # grab the files from the folder and run the pipeline
    for path in glob('input/*'):
        target_dir = Path(path).stem
        print(f'Building with path: {path!r}, target: {target_dir!r}')
        dag = DAGSpec('pipeline.yaml',
                      env={
                          'input_path': path,
                          'target_dir': target_dir
                      }).to_dag()
        dag.build()


if __name__ == '__main__':
    while True:
        print('Checking for new files...')
        run()
        print('Sleeping...')
        time.sleep(5)