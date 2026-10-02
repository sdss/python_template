# Python Source Guidance

This directory contains the generated package source; package code lives inssude the `src` subdirectory.

- Keep package code inside the package directory and follow the SDSS Python coding standards.
- Use type hints and clear, descriptive names; keep public APIs intentional and documented.
- Add or update focused tests under `tests/` when changing behavior. Use `pytest` to run tests and generate coverage reports.
- Use Ruff for linting and formatting, and run the project's tests with its documented development dependencies available.
- Avoid adding dependencies unless the project needs them; declare required dependencies in `pyproject.toml`.
