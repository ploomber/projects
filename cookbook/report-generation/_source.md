---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.2
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Report generation

<!-- start description -->
Generating HTML/PDF reports.
<!-- end description -->

Ploomber makes it simple to generate HTML and PDF reports from notebooks and scripts. To see some examples, go to the `reports/` directory. This cookbook covers several use cases and includes runnable examples.

## HTML reports (easiest option)

HTML reports are the simplest option as they don't require any extra dependencies. You only need to change the `product` extension to `.html` and Ploomber will do the conversion:

<% expand('pipeline.yaml', lines=(2, 7)) %>

Runnable example:

<!-- #md -->
```sh
# get example
pip install ploomber "nbconvert[webpdf]" --upgrade
ploomber examples -n cookbook/report-generation -o example
cd example

# install example dependencies
ploomber install

# generate HTML report
ploomber task html-report
```
<!-- #endmd -->

Check out report at `reports/report.html`

## PDF reports

To generate PDF reports there are two options, using chromium or TeX.

### Using chromium (easiest pdf option)

To use use chromium, pass `nbconvert_exporter_name: webpdf`

<% expand('pipeline.yaml', lines=(26, 33)) %>

Runnable example:

<!-- #md -->
```sh
# get example
pip install ploomber "nbconvert[webpdf]" --upgrade
ploomber examples -n cookbook/report-generation -o example
cd example

# install example dependencies
ploomber install

# generate PDF report
ploomber task webpdf-report
```
<!-- #endmd -->

Check out report at `reports/report-webpdf.pdf`

### Using TeX

TeX is the default, to use it, set the product extension to `.pdf`:

<% expand('pipeline.yaml', lines=(35, 40)) %>

Runnable example:

<!-- #md -->
```sh
# get example
pip install ploomber "nbconvert[webpdf]" --upgrade
ploomber examples -n cookbook/report-generation -o example
cd example

# install example dependencies
ploomber install

# generate PDF report
ploomber task pdf-report
```
<!-- #endmd -->

Check out report at `reports/report.pdf`

#### Installing TeX

For instructions on installing TeX, [see this.](https://www.tug.org/texlive/).

TeXLive is a large distribution, as an alternative, you may install BasicTeX. Here are instructions for [macOS](https://www.tug.org/mactex/morepackages.html).

Upon BasicTeX installation, you'll need to install a few extra packages:

<!-- #md -->
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
<!-- #endmd -->

[Source.](https://github.com/jupyter/nbconvert/issues/1328)

## Hiding code

In many cases, you want to hide the code so the report only contains tables and charts, you can do so easily with the `exclude_input` option:

<% expand('pipeline.yaml', lines=(9, 17)) %>

Runnable example:

<!-- #md -->
```sh
# get example
pip install ploomber "nbconvert[webpdf]" --upgrade
ploomber examples -n cookbook/report-generation -o example
cd example

# install example dependencies
ploomber install

# generate HTML report and hide code
ploomber task another-html-report
```
<!-- #endmd -->

Check out report at `reports/another.html`

## Hiding cells

You may want to hide cells from the output notebook selectively. You can do so with the `TagRemovePreprocessor`, which takes a list of tags. Any cells with such tags are excluded:

<% expand('pipeline.yaml', lines=(9, 24)) %>

To learn how to add cell tags, [see this.](https://ploomber.io/s/tags)

Runnable example:

<!-- #md -->
```sh
# get example
pip install ploomber "nbconvert[webpdf]" --upgrade
ploomber examples -n cookbook/report-generation -o example
cd example

# install example dependencies
ploomber install

# generate HTML report and hide boxplot
ploomber task another-html-report
```
<!-- #endmd -->

Check out report at `reports/another.html`