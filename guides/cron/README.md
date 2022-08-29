<!-- start header -->
To run this example locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/quick-start.html) and execute: `ploomber examples -n guides/cron`

To start a free, hosted JupyterLab: [![binder-logo](https://raw.githubusercontent.com/ploomber/projects/master/_static/open-in-jupyterlab.svg)](https://binder.ploomber.io/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fguides/cron%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=guides/cron%20issue)

Have questions? [Ask us anything on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/guides/cron/README.ipynb)
<!-- end header -->



# Scheduling with cron

This guide shows how to schedule Ploomber pipelines using `cron`.

**Note:** `cron` is only available on macOS and Linux.

## Pre-requisites

Ensure cron is installed:

<!-- #md -->
```sh
crontab -l
```
<!-- #endmd -->

If you don't see a "command not found error", you have `cron` installed and can continue.

## Get the example

<!-- #md -->
```sh
pip install ploomber
ploomber examples -n guides/cron -o cron
cd cron
```
<!-- #endmd -->

## Setup

Configure virtual environment:

<!-- #md -->
```sh
ploomber install --create-env --use-venv
```
<!-- #endmd -->

Activate environment:

<!-- #md -->
```sh
source venv-cron/bin/activate
```
<!-- #endmd -->

## The code

The pipeline has two stages: load, and plot:

<!-- #md -->
```yaml
# Content of pipeline.yaml
tasks:
  - source: scripts/load.py
    product:
      nb: products/{{timestamp}}/load.html
      data: products/{{timestamp}}/load.csv

  - source: scripts/plot.py
    product:
      nb: products/{{timestamp}}/plot.html
```
<!-- #endmd -->


Notice that all the products are parametrized prefixed by: `products/{{timestamp}}`; this will allow us to store the products of each run depending on the runtime timestamp.

## Development

When modifying the pipeline, you can call the following command:

```sh
ploomber build
```

Note that products will go to `output/dev/`.

For scheduling the workflow, we need to tell Ploomber to use a different configuration file:

```sh
# tell ploomber to use env.cron.yaml as config file
export PLOOMBER_ENV_FILENAME=env.cron.yaml
# build pipeline
ploomber build
# delete env variable
unset PLOOMBER_ENV_FILENAME
```

Let's see the contents of the products directory:

```sh
ls products
```

You should see two folders, `dev/` and another one with the runtime timestamp.


## Scheduling

Now let's schedule in cron. First, to edit the cron configuration file:

<!-- #md -->
```sh
crontab -e
```
<!-- #endmd -->

Note that this will open the configuration file in the default editor,
if you don't know what that is, you can open it with `nano`:

<!-- #md -->
```sh
EDITOR=nano crontab -e
```
<!-- #endmd -->

Once the editor opens, add a line like this:

```txt
* * * * *  PROJ=/path/to/cron && cd $PROJ && bash run.sh >> cron.log 2>&1
```

**Note:** If using macOS Big Sur (11.6) or newer, you may need to follow a few [extra steps](https://osxdaily.com/2020/04/27/fix-cron-permissions-macos-full-disk-access/) to enable cron.


Replace the `/path/to/cron/` with the absolute path to the `cron/` directory that contains the sample code. (Tip: so get the absolute path, enter `pwd` in your terminal).

If you opened the configuration file with `nano`, save your changes with `CTRL + O` and exit the editor with `CTRL + X`.

After a minute, you'll start to see more directories in the products folder; this is what mine looks like:

```
2022-03-12T11:14:47.506532/ 
2022-03-12T11:25:12.707618/ 
dev/
```

If you see something like this, congratulations, you have a scheduled pipeline up and running!

To learn how to modify the scheduling interval, see the Overview section in cron's [Wikipedia article.](https://en.wikipedia.org/wiki/Cron)


## Troubleshooting

If you don't see the new directories, check out the `cron.log` file, which will contain any error messages, and ping us [on Slack](https://ploomber.io/community) so we can help you.
