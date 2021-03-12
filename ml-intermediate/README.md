# Intermediate ML project

Training and serving ML pipeline with integration testing.

## Setup

~~~bash
# if using conda
conda env create --file environment.yml
conda activate ml-intermediate

# or use pip directly
pip install -r requirements.txt
~~~

## Build

```bash tags=["bash"]
ploomber build
```

## Serving

Once the model is trained, run the serving pipeline with:

```bash tags=["bash"]
ploomber build --entry-point pipeline-serve.yaml
```

This pipeline loads some data and uses the model file to make predictions.
