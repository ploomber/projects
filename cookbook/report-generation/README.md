<!-- start header -->
To run this example locally, [install Ploomber](https://docs.ploomber.io/en/latest/get-started/install.html) and execute: `ploomber examples -n cookbook/report-generation`

To start a free, hosted JupyterLab: [![binder-logo](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ploomber/binder-env/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fploomber%252Fprojects%26urlpath%3Dlab%252Ftree%252Fprojects%252Fcookbook/report-generation%252FREADME.ipynb%26branch%3Dmaster)

Found an issue? [Let us know.](https://github.com/ploomber/projects/issues/new?title=cookbook/report-generation%20issue)

Have questions? [Ask us anything on Slack.](https://ploomber.io/community/)

For a notebook version (with outputs) of this file, [click here](https://github.com/ploomber/projects/blob/master/cookbook/report-generation/README.ipynb)
<!-- end header -->



# Report generation

<!-- start description -->
Generating HTML/PDF reports.
<!-- end description -->

Ploomber makes it simple to generate HTML and PDF reports from notebooks and scripts. To see some examples, go to the `reports/` directory.

Here's a sample `pipeline.yaml` that shows various use cases:

<!-- #md -->
```yaml
# Content of pipeline.yaml
tasks:
    # scripts can generate reports
    - source: tasks/script.py
      name: html-report
      product:
        nb: reports/report.html
        # the task can generate more outputs, list them here
    
    # notebooks as well
    - source: tasks/notebook.ipynb
      name: another-html-report
      product:
        nb: reports/another.html

      nbconvert_export_kwargs:
        # optionally hide the code from the report
        exclude_input: True
      
        # optionally, exclude cells with certain tags
        config:
          HTMLExporter:
            preprocessors: [nbconvert.preprocessors.TagRemovePreprocessor]
          TagRemovePreprocessor:
            remove_cell_tags: [boxplot]

    # pdf report example
    - source: tasks/script.py
      name: webpdf-report
      # use the webpdf exporter (supportes embedded charts)
      # (it will download chromium if needed)
      nbconvert_exporter_name: webpdf
      product:
        nb: reports/report-webpdf.pdf

    # pdf report example (requires latex)
    - source: tasks/script.py
      name: pdf-report
      # generate pdf report by changing the extension.
      product:
        nb: reports/report.pdf

    # skip report generation
    - source: tasks/download.py
      name: no-report
      # run as a script. Do not generate output report
      # Note: ScriptRunner was introduced in Ploomber 0.17.2
      class: ScriptRunner
      product:
        data: data/data-another.csv
    
```
<!-- #endmd -->


## HTML reports (no config needed)

HTML reports are the simplest option as they don't require any extra dependencies. You only need to change the `product` extension to `.html` and Ploomber will do the conversion:

<!-- #md -->
```yaml
# Content of pipeline.yaml
    # scripts can generate reports
    - source: tasks/script.py
      name: html-report
      product:
        nb: reports/report.html
        # the task can generate more outputs, list them here
```
<!-- #endmd -->

<!-- #region -->
## PDF reports

To generate PDF reports there are two options, using chromium or TeX.

### Using chromium (easiest to configure)

To use use chromium, pass `nbconvert_exporter_name: webpdf`

<!-- #md -->
```yaml
# Content of pipeline.yaml
    # pdf report example
    - source: tasks/script.py
      name: webpdf-report
      # use the webpdf exporter (supportes embedded charts)
      # (it will download chromium if needed)
      nbconvert_exporter_name: webpdf
      product:
        nb: reports/report-webpdf.pdf
```
<!-- #endmd -->

### Using TeX

TeX is the default, to use it, set the product extension to `.pdf`:

<!-- #md -->
```yaml
# Content of pipeline.yaml
    # pdf report example (requires latex)
    - source: tasks/script.py
      name: pdf-report
      # generate pdf report by changing the extension.
      product:
        nb: reports/report.pdf
```
<!-- #endmd -->

For instructions on installing TeX, [see this.](https://www.tug.org/texlive/).

TeXLive is a large distribution, as an alternative, you may install BasicTeX. Here are instructions for [macOS](https://www.tug.org/mactex/morepackages.html).

Upon BasicTeX installation, you'll need to install a few extra packages:

```sh
# Note: if using macOS or Linux, you may need to execute with sudo
tlmgr install adjustbox \
  caption \
  collectbox \
  enumitem \
  environ \
  eurosym \
  jknapltx \
  parskip \
  pgf \
  rsfs \
  tcolorbox \
  titling \
  trimspaces \
  ucs \
  ulem \
  upquote 
```

[Source.](https://github.com/jupyter/nbconvert/issues/1328)
<!-- #endregion -->

## Hiding code

In many cases, you want to hide the code so the report only contains tables and charts, you can do so easily with the `exclude_input` option:

<!-- #md -->
```yaml
# Content of pipeline.yaml
    # notebooks as well
    - source: tasks/notebook.ipynb
      name: another-html-report
      product:
        nb: reports/another.html

      nbconvert_export_kwargs:
        # optionally hide the code from the report
        exclude_input: True
```
<!-- #endmd -->


## Hiding cells

You may want to selectively hide cells from the output notebook. For example. You can do so with the `TagRemovePreprocessor`, which takes a list of tags. Any cells with such tags are excluded.

To learn how to add cell tags, [see this.](https://ploomber.io/s/tags)

Here's a full example:

<!-- #md -->
```yaml
# Content of pipeline.yaml
    # notebooks as well
    - source: tasks/notebook.ipynb
      name: another-html-report
      product:
        nb: reports/another.html

      nbconvert_export_kwargs:
        # optionally hide the code from the report
        exclude_input: True
      
        # optionally, exclude cells with certain tags
        config:
          HTMLExporter:
            preprocessors: [nbconvert.preprocessors.TagRemovePreprocessor]
          TagRemovePreprocessor:
            remove_cell_tags: [boxplot]
```
<!-- #endmd -->