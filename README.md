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

If you answered yes to the question "Create a virtual env and sync the project after creation using uv" your project will already be synced to a virtual environment in the same directory as the project. If you need to create the venv and sync manually, go to the project directory and run:

```console
uv venv
uv sync --all-extras --all-groups
```

This will create a virtual environment in `.venv/` and install the project along with all the dependencies.

## What you get in this template

* A basic Python 3 template with a `pyproject.toml` file using [uv](https://docs.astral.sh/uv) as build system and dependency manager.
* Linting and formatting using [ruff](https://docs.astral.sh/ruff) with rules that meet the [SDSS coding standards](style/STYLE_v2).
* Post-copy scripts to create a remote repository for your project.
* Ready-to-write and -deploy Sphinx documentation using the [furo](https://github.com/pradyunsg/furo) theme.
* Unit-testing using [pytest](https://docs.pytest.org/en/stable/).
* GitHub Actions workflows for linting, testing, and deployment.

## Coding standards

Before you start writing your code, make sure to read and understand the [SDSS coding standards](https://sdss-python-template.readthedocs.io/en/latest/style/STYLE_v2.html).

## Building the documentation

The template include a stub for [Sphinx](https://www.sphinx-doc.org/en/master/) documentation under `docs/sphinx`. To build the documentation locally, run the following command from the project root:

```console
sdss docs.build
```

To have the docs autobuild and watch for changes, use `nox`. To build and run the local docs server, run

```console
nox
```

This will start a local docs server on a random port. You should see something like,

```console
[sphinx-autobuild] Serving on http://127.0.0.1:54429
[sphinx-autobuild] Waiting to detect changes...
```

It should open the site automatically in a new browser window.  If `127.0.0.1:[port]` fails to load, try `localhost:[port]`.

Additional information on how to build the documentation can be found in the [docs](https://sdss-python-template.readthedocs.io/en/latest/index.html#package-documentation) section of the documentation.
