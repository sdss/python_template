# Python Source Guidance

This package is a [Copier](https://copier.readthedocs.io/en/stable/) template to create new Python packages for the SDSS project. Documentation on how to use the template can be found in the `README.md` file in the `docs/` directory.

## Project structure

- The template can be found in the `template/` directory. The template uses [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) syntax to render the files in the template.
- The `copier.yaml` file contains the questions that will be asked when creating a new project from the template. The answers to these questions will be used to render the files in the template.
- The `template/post_copy.py` file contains the post-copy tasks that will be run after the template is copied to the destination directory. These tasks can be used to set up the new project, such as creating a virtual environment, installing dependencies, and initializing a Git repository.
- The documentation for the template itself can be found in `docs/` and is built using [Sphinx](https://www.sphinx-doc.org/en/master/).

## Environment

- The project uses [uv](https://github.com/astral-sh/uv) to manage the dependencies needed to render the template and build the documentation.
- All package information can be found in `pyproject.toml`, including dependencies, versioning, and package metadata.
- Use `uv run` to run commands in the virtual environment. This will create a virtual environment if one does not exist, and will install dependencies if they are missing.
- Use `uv sync` to synchronize the virtual environment with the dependencies in `pyproject.toml`.
- Use `uv add` to add a new dependency to the project and install it in the virtual environment.

## Template

- The template uses [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) syntax to render the files in the template. The template can be found in the `template/` directory.
- To render the template and create a new project, use the `copier` command, e.g., `uvx copier copy --trust gh:sdss/python_template <path-to-root>/test_project`.

## Documentation

- Documentation is written in [Sphinx](https://www.sphinx-doc.org/en/master/) format and can be built running `make` from the `docs/sphinx/` directory.
- The documentation is deployed to [Read the Docs](https://readthedocs.org/). The configuration file is located in `readthedocs.yaml`.

## Linting and formatting

- The project uses [ruff](https://github.com/astral-sh/ruff) for linting and formatting.
- The configuration for linting and formatting is located in `pyproject.toml`.
- Use `uv run ruff check` to check for linting issues, and `uv run ruff format --check` to check for formatting issues.
