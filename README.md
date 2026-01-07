# SDSS Python Template

This is a [copier](https://copier.readthedocs.io/en/stable/) template for creating Python packages that adhere to the [SDSS standards](https://sdss-python-template.readthedocs.io/en/latest/style/STYLE_v2.html).

The full documentation on how to use this template can be found [here](http://sdss-python-template.readthedocs.io/en/latest/).

> **WARNING:** version 3 of the Python Template is significantly different from previous versions. Check the documentation for details on the changes and how to migrate from version 2 to version 3.

## User Installation

To install and copy this template we recommend first installing [uv](https://docs.astral.sh/uv)

```console
curl -LsSf https://astral.sh/uv/install.sh | sh
```

You can then install `copier` using `uv`:

```console
uv tool install -U copier
```

To create a new project `test_project`, run:

```console
uvx copier copy --trust gh:sdss/python_template <path-to-root>/test_project
```

Note that you'll want to include the `--trust` flag to allow the post-copy tasks to run. The destination must include the project name, e.g. `~/software/test_project`. Copier will ask a few questions and then will copy the rendered template to the destination folder.

## What you get in this template

* A basic Python 3 template with a `pyproject.toml` file using [uv](https://docs.astral.sh/uv) as build system and dependency manager.
* Linting and formatting using [ruff](https://docs.astral.sh/ruff) with rules that meet the [SDSS coding standards](style/STYLE_v2).
* Post-copy scripts to create a remote repository for your project.
* Ready-to-write and -deploy Sphinx documentation using the [furo](https://github.com/pradyunsg/furo) theme.
* Unit-testing using [pytest](https://docs.pytest.org/en/stable/).
* GitHub Actions workflows for linting, testing, and deployment.

## Coding standards

Before you start writing your code, make sure to read and understand the [SDSS coding standards](https://sdss-python-template.readthedocs.io/en/latest/style/STYLE_v2.html).
