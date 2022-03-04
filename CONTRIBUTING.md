# Contributing

## Setup your env with conda

The simplest way to setup the environment is via conda. [Click here for miniconda installation details](https://docs.conda.io/en/latest/miniconda.html).


```sh
# invoke is needed to run the next command
pip install invoke

# install dependencies
invoke setup
```

Then activate the environment:

```sh
conda activate projects
```

## Updating root README.md

To update the root `README.md`, modify `_source.md`. Then execute the following command:

```sh
invoke build --name readme
```

Note that `ploomber examples` uses `index.csv` to list available examples.

## Types of examples

We classify examples depending on their objective:

1. `cookbook`: Short and to-the-point examples showing how to achieve something specific. These are for users to get some sample code that they can incorporate into their projects.
2. `tutorials`: Long, in-depth tutorials for learning. These teach users concepts and features in-depth; some of these are part of the documentation itself, the introductory ones are part of the *Get Started* section, while the more advanced ones are part of the *User Guide*. Some of these are related and have an order to set the *learning journey*: users learn something basic, then move on to something more advanced. If tutorials are related, they should link to each other.
3. `templates`: They're are halfway through `cookbook` and `tutorials`. They're starting points for new projects; hence, they achieve something specific but have a high-level explanation of each part so users can understand it and customize it quickly. Templates may be related (e.g., a template for an ML regression problem and one for a classification problem), but the relationship is unordered; they are suggestions for users to explore related content. Relatec tutorials should link each other.

## Adding examples

Each project must have the same layout:

Required:

* `environment.yml` - Conda environment spec

```yaml
name: {example-name}

dependencies:
  
  - pip

  - pip:
    - ploomber
    # other dependencies...
```

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

#### Title and description

Next to the front matter, you should include a title and a description:

```md
# This is a title

<!-- start description -->
This is a description.
<!-- end description -->

```

Note that the description is enclosed between two special marks (`<!-- start/end description -->`). The marks are necessary because we use them to identify the description and compile the root `README.md` from `_source.md`.

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
