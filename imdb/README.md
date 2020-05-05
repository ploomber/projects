# IMDB pipeline

## Installation


```sh
# create conda environment
conda env create --file environment.yml

# install project package inside the conda env
conda activate imdb
pip install .
```

## Execute pipeline

Edit `env.yaml`

```sh
python -m ploomber.entry imdb_project.pipeline.pipeline.make build
```