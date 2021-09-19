# Basic ML project

Machine Learning pipeline.

## Setup

(**Note**: Skip if running in Binder)

~~~bash
# if using conda
conda env create --file environment.yml
conda activate ml-basic

# or use pip directly
pip install -r requirements.txt
~~~

## Description

Let's take a look at the `pipeline.yaml`:

```bash tags=["bash"]
cat pipeline.yaml
```

Note that the first three tasks as Python functions, while the last one is a
script.

Generate the plot:

```bash tags=["bash"]
ploomber plot
```

```python
# If using jupyter, you can show the plot with this code:
from IPython.display import Image
Image(filename='pipeline.png')

# otherwise open the pipeline.png file directly
```

## Build pipeline

```bash tags=["bash"]
ploomber build
```

Since the training task is a script, it will generate a Jupyter notebook at
[output/nb.ipynb](output/nb.ipynb) with evaluation charts.

## Interacting with the pipeline

The command line interface is a convenient way to interact with your
pipeline. Try this in a terminal:

~~~bash
ploomber interact
~~~
