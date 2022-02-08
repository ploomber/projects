
This pipeline polls a folder and it processes them whenever it finds a new one.

## Setup

```sh
# install ploomber
pip install ploomber

# download example
ploomber examples -b batch -n cookbook/directory-polling -o polling
```

## Runnning the example

In one terminal, run:

```sh
python run.py
```

It won't do anything since there are no files to process. Keep it running,
and in a new terminal:

```sh
python create_data.py
```

You'll see that `run.py` locates the file and processes it.

Execute `python create_data.py` more times to see that `run.py` processes new files as they arrive!
