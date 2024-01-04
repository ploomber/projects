<!-- start header -->
To run this locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n cookbook/file-client`

Questions? [Ask us on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/cookbook/file-client/README.ipynb)
<!-- end header -->



# File client

<!-- start description -->
Upload task's products upon execution (local, S3, GCloud storage)
<!-- end description -->

Run the pipeline:

```sh
ploomber build
```

The pipeline has a `LocalStorageClient` configured; you'll see a copy of the
products in the `backup` directory. See the `pipeline.yaml` to see how to
switch to S3 and Google Cloud Storage.
