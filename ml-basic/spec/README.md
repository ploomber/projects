# Basic ML project (Spec API)

This example shows how to build the same ML pipeline but this time using the
Spec API (`pipeline.yaml`) instead of the Python API. It uses the same source
code as the other version.

## Setup

```bash
# same instructions as the other version
git clone https://github.com/ploomber/projects
cd ml-basic
pip install .
```

## Executing pipeline

This part is different

```bash
# make sure you move to the spec folder
cd spec

# folder to save output
mkdir output

# execute using the spec file
ploomber build --entry-point pipeline.yaml
```
