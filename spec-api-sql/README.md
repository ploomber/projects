# SQL/Python pipeline

Pipeline with SQL and Python tasks.

## Setup

(**Note**: Skip if running in Binder)

~~~sh
# if using conda
conda env create --file environment.yaml
conda activate spec-api-sql

# or use pip directly
# note that this won't install pygraphviz. If you want to plot the pipeline
# you have to install it first
pip install -r requirements.txt
~~~

## Create sample data


```bash tags=["bash"]
# create sample data
cd setup
bash setup.sh
# move back to the original spec-api-sql folder
cd ..
```

## Definition

```bash tags=["bash"]
cat pipeline.yaml
```
The first two sections configure our pipeline; the `tasks` section is the
actual pipeline definition. We see that we have a few SQL transformations,
then we dump a table to a CSV file and we produce an HTML report at the end.
The order here doesn't matter, the source code itself declares its own
upstream dependencies, and Ploomber extracts them to execute your pipeline.


## Plot

```bash tags=["bash"]
# Note: if plotting locally, install pygrapviz first
ploomber plot
```

If running in Jupyter, load the plot with this code:

```python
from IPython.display import Image
Image(filename='pipeline.png')
```

Otherwise, open the `pipeline.png` file directly.


## Build

```bash tags=["bash"]
ploomber build
```
The final output is a report: [output/plot.html](output/plot.html).
