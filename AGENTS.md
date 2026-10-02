# Repository Guidance

This repository maintains the SDSS Python Copier template. The `template/` directory is the source for files copied into generated projects; `copier.yaml` defines the questions and rendering configuration.

- Do not confuse this `AGENTS.md` file with the `AGENTS.md` file in the `template/` directory, which is copied into generated projects.
- Keep generated-project changes in `template/`, preserving Jinja syntax and Copier variables where needed.
- Keep template-maintainer code and documentation outside `template/` unless they are intended to be copied into every generated project.
- Follow the SDSS Python coding standards documented in `docs/sphinx/style/` and keep changes focused.
- When changing rendered files, check the result with a Copier render or the relevant template validation before finishing.
- Do not commit generated artifacts, local environments, or unrelated workspace changes.
