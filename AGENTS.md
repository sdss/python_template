# Repository Guidance



This package was generated using the [SDSS Python package template](https://github.com/sdss/python_template). Read the README.md file for more information about the purpose of this package and how to use it.

## Project structure

- The Python code lives inside the `src/` directory.
- Tests can be found in the `tests/` directory.
- Documentation in Sphinx format is located in the `docs/sphinx/` directory.
- GitHub Actions workflows are located in the `.github/workflows/` directory.

## Environment

- The project uses [uv](https://github.com/astral-sh/uv) for package and virtual environment management.
- All package information can be found in `pyproject.toml`, including dependencies, versioning, and package metadata.
- Use `uv run` to run commands in the virtual environment. This will create a virtual environment if one does not exist, and will install dependencies if they are missing.
- Use `uv sync` to synchronize the virtual environment with the dependencies in `pyproject.toml`.
- Use `uv add` to add a new dependency to the project and install it in the virtual environment.

## Tests

- Tests are written using [pytest](https://docs.pytest.org/en/) and can be run with `uv run pytest`.
- Keep tests in the `tests/` directory, and name them starting with `test_` so that pytest can discover them.
- Tests should be written to be as independent as possible, so that they can be run in any order. Use fixtures to set up and tear down test environments as needed.

## Documentation

- Documentation is written in [Sphinx](https://www.sphinx-doc.org/en/master/) format and can be built running `make` from the `docs/sphinx/` directory.
- The documentation is deployed to [Read the Docs](https://readthedocs.org/). The configuration file is located in `readthedocs.yaml`.

## Linting and formatting

- The project uses [ruff](https://github.com/astral-sh/ruff) for linting and formatting.
- The configuration for linting and formatting is located in `pyproject.toml`.
- Use `uv run ruff check` to check for linting issues, and `uv run ruff format --check` to check for formatting issues.
