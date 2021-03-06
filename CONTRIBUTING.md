# Contributing

Each project must have the same layout:

Required:

* `environment.yml` - Conda environment spec
* `README.md` - Instructions to execute the project
* `output/` - All output files should be stored in a relative folder named `output`

Optional:

* `pipeline.yaml` - If the example uses the Spec API
* `setup/script.sh` - Bash script to run any pre-execution steps (`script.py` also works), it is executed with `setup/` as the current working directory

# Building

1. Generate README.md from README-template.md and index.csv
2. Execute all */README.md files (to generate */README.ipynb)
3. Generate requirements.txt from environment.yml (for people who don't use conda)
4. Generate repository-level requirements.txt and environment.yml for binder and deepnote

**Note:** The repository-level environment.yml is saved in a different repo to allow
quick Binder loading.

```sh
invoke build
```

```sh
invoke build --force
```

# Root README.md

The root `README.md` is generated from
`pkg/src/ploomberutils/README-template.md` and `index.csv`.

# Example README.md guidelines

`README.md` are converted to Jupyter notebooks and executed to test them and show the output of each command. Some of these files are also displayed in Ploomber's documentation.

Jupyter can execute bash scripts but given that jupytext loses the language
markdown tag when it converts from .md to .ipynb, we have to indicate the
language using a tag:

```bash tags=["bash"]
echo 'hello'
```

To prevent a cell from executing use `~~~`:

~~~bash
# this won't be executed
~~~

Note: from the many [alternatives](https://jupytext.readthedocs.io/en/latest/formats.html#jupytext-markdown),
we selected the `~~~` option because it's the only one that produces notebooks that correctly render on Github.

The output is stored as `README.ipynb`. Which is the file that you should
point to share binder links.

# Tutorials

Some folder are not actual examples but tutorials that are part of the
documentation: debugging, parametrized, testing and sql-templating.