<!-- start header -->
To run this locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n cookbook/dynamic-params`

Questions? [Ask us on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/cookbook/dynamic-params/README.ipynb)
<!-- end header -->



# Dynamic params

<!-- start description -->
Pipeline parameters whose values are computed at runtime.
<!-- end description -->

Run the pipeline:

```sh
python run.py
```

Check output (stored in directory with name `0`):

```sh
ls products
```

Run again:

```sh
python run.py
```

Check output (this time, stored in directory with name `1`):

```sh
ls products
```
