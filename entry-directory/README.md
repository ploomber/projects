# Directory as entry point

This example shows how you can build a pipeline from a directory with scripts
(without defining a `pipeline.yaml` file):

```sh
mkdir output
ploomber build --entry-point .
```