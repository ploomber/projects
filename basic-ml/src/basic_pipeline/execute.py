from pathlib import Path
import argparse

from basic_pipeline import pipeline


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('path', type=str,
                        help='Path to the output folder')

    args = parser.parse_args()
    path = Path(args.path)

    print('Output will be stored in: ', path.resolve())

    if not path.exists():
        print('Creating folder...')
        path.mkdir(exist_ok=True, parents=True)

    print('Running pipeline...')
    pipeline.make(path).build()
