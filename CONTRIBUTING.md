# Contributing

Each project must have the same layout:

Required:

* `environment.yml` - Conda environment spec
* `README.md` - Instructions to execute the project
* `output/` - All output files should be stored in a relative folder named `output`

Optional:

* `pipeline.yaml` - If the example uses the Spec API
* `setup/script.sh` - Bash script to run any pre-execution steps (`script.py` also works), it is executed with `setup/` as the current working directory


# README.md guidelines

`README.md` are converted to Jupyter notebooks and executed to show users
the output of each one.

Jupyter can execute bash scripts but given that jupytext loses the language
markdown tag when it converts from .md to .ipynb, we have to indicate the
language using a tag:

```bash tags=["bash"]
echo 'hello'
```

To prevent a cell from executing add `.noeval`

```bash .noeval
# this won't be executed
```

The output is stored as `README.ipynb`. Which is the file that you should
point to share binder links.