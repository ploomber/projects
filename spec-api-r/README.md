# R pipeline

R pipeline.

## Setup environment

(**Note**: Skip if running in Binder)

~~~sh
# if using conda (installs R in the virtual env)
conda env create --file environment.yaml
conda activate spec-api-r

# if using pip, you need to install R manual and set up the IRKernel
# package manually: https://github.com/IRkernel/IRkernel, then
pip install -r requirements.txt
~~~

## Pipeline description

This pipeline contains three tasks. The last task generates a plot. To get the
pipeline description:

```bash tags=["bash"]
ploomber status
```

## Build the pipeline from the command line

```bash tags=["bash"]
mkdir output
ploomber build
```

Output stored in the ``output/`` directory.
