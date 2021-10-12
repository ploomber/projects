# Contributing

## Updating root README.md

To update the root `README.md`, modify `_source.md`. Then execute the following command:

```sh
invoke build --name readme
```

Note that `ploomber examples` uses `index.csv` to list available examples.

## Documentation tutorials

Some directories are not examples but tutorials that are part of the documentation: debugging, parametrized, testing and sql-templating.

## Adding examples

Each project must have the same layout:

Required:

* `environment.yml` - Conda environment spec
* `README.md` - Instructions to execute the project
* `output/` - All output files should be stored in a relative folder named `output`

Optional:

* `pipeline.yaml` - If the example uses the Spec API
* `setup/script.sh` - Bash script to run any pre-execution steps (`script.py` also works), it is executed with `setup/` as the current working directory


After adding an example, include it in the `ci.yml` to run it on each push.

### Guidelines for new examples

You should create a `_source.md` file at the root of the example. This file generates the `README.md`, which contains a header with links and resolves references to external files (more on this below).

Using the `README.md`, we generate the `README.ipynb` and execute it. Here are the guidelines for the `_source.md` file:

Once a new example is included, you must add a new entry to `index.csv`.

#### Front matter

Add this to the top of the `_source.md`, this is necessary for the conversion to `README.md` (note the `---` at the beginning and the end).

```
---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---
```

#### Setup instructions

*Do not* include a section to show how to setup the example (e.g., `pip install ...`).

#### Skip execution

After generating the `README.ipynb`, it is executed. To skip execution of certain code chunk, enclose it using the following tags:

```md
<!-- #md -->

<!-- Your code snippet -->

<!-- #endmd -->
```

#### Reference other files

If you need to reference external files, do not copy their content; use the following instead:

```md

README.md will add the contents here:
<% expand('some_file.py') %>

To select specific symbols like function definitions (only works with .py files):
<% expand('some_file.py', symbols='some_function') %>
<% expand('some_file.py', symbols=['some_function', 'another']) %>

To select specific lines:
<% expand('some_file.py', lines=(10, 15)) %>
```

*Note:* code chunks added this way are not executed (see previous section).


## Building process

1. Generate root README.md from README-template.md and index.csv
2. Compile all */_source.md files (to generate */README.md)
2. Execute all */README.md files (to generate */README.ipynb)
3. Generate requirements.txt from environment.yml
4. Generate repository-level requirements.txt and environment.yml for binder

**Note:** The repository-level environment.yml is saved in a different repo to allow
quick Binder loading.


To build:

```sh
invoke build
```

```sh
invoke build --force
```
