# Pipeline from directory

Pipeline from a directory of scripts.

## Setup

(**Note**: Skip if running in binder or deepnote)

~~~sh
# if using conda
conda env create --file environment.yaml
conda activate spec-api-directory

# or use pip directly
pip install -r requirements.txt
~~~

## Build

```bash tags=["bash"]
mkdir output
ploomber build --entry-point '*.py'
```

Output stored in the `output/` directory.


## Describe

This pipeline contains five steps. The last task trains a model and outputs a
report and a model file. To get the pipeline description:

```bash tags=["bash"]
ploomber status --entry-point '*.py'
```

`--entry-point '*.py'` means "all files with py extension are tasks in the
pipeline". If all the files in the current directory are tasks, you can also
use the shortcut `--entry-point .`.
