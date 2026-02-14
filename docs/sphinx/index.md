
# SDSS Python Template

```{toctree}
:hidden:
Changelog <changelog>
Style guide <style/STYLE_v2>
```


```{warning}
This is the documentation for the SDSS Python Template version 3. The documentation for version 1 can be found [here](https://sdss-python-template.readthedocs.io/en/2.1.0) and for version 2 [here](https://sdss-python-template.readthedocs.io/en/1.0.6).
```

The SDSS Python Template is a ready-to-use template for creating Python packages
that follow best practices and SDSS guidelines. We use [Copier](https://copier.readthedocs.io/en/stable/) to render the template. Since this template assumes that you will be using [uv](https://docs.astral.sh/uv), the easiest way is to first [install uv](https://docs.astral.sh/uv/getting-started/installation/) with

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

and then install Copier with

```bash
uv tool install -U copier
```

To create a new project `test_project`, run:

```bash
uvx copier copy --trust gh:sdss/python_template <path-to-root>/test_project
```

Note that you'll want to include the `--trust` flag to allow the post-copy tasks to run. The destination must include the project name, e.g. `~/software/test_project`. Copier will ask a few questions and then will copy the rendered template to the destination folder.

## Goals of the template

The goal of the SDSS Python Template is to provide a lightweight template that conforms to the SDSS coding standards and that includes everything that you need to start a new coding project without a lot of extra features that you might not need. The template provides:

* A basic Python 3 template with a `pyproject.toml` file using [uv](https://docs.astral.sh/uv) as build system and dependency manager.
* Linting and formatting using [ruff](https://docs.astral.sh/ruff) with rules that meet the [SDSS coding standards](style/STYLE_v2).
* Post-copy scripts to create a remote repository for your project.
* Ready-to-write and -deploy Sphinx documentation using the [furo](https://github.com/pradyunsg/furo) theme.
* Unit-testing using [pytest](https://docs.pytest.org/en/stable/).
* GitHub Actions workflows for linting, testing, and deployment.
* A `Dockerfile` and GitHub Actions workflow for building and publishing a Docker image to the GitHub Container Registry.

Version 3 of the template is somewhat more opinionated than previous versions and supports fewer configuration options. This is partly to streamline the process of creating a new project and partly because in recent years the Python community has consolidated around a set of tools (uv, Ruff, pytest) for development. Our philosophy is that if you have strong opinions about what tools to use it is probably trivial for you to modify the rendered template to meet your needs.

Please, [open an issue](https://github.com/sdss/python_template/issues/new) if you think that something important is missing from the template or if you find a bug.

## Customizing the rendered template

When your run the `copier copy` command you will be asked a series of questions about the name of the project, author information, etc. Here is an example of the questions and answers:

```text
$ uvx copier copy --trust gh:sdss/python_template ~/Downloads/my_project
📚 The name of the project. Used as repository name, in documentation, and other places.
   my_project
📦 The name of the Python package to create. This is the import name and the name of the package in PyPI.
   my_package
📝 A short description of the project.
   A wonderful new tool
🙋 The full name of the project maintainer.
   John Smith
📧 The email of the project maintainer.
   john-smith@university.edu
⚖️ The license for the project.
   BSD-3-Clause
🐙 The GitHub organization or user where the repository will be hosted.
   sdss
👤 The GitHub username of the project maintainer.
   albireox
🚀 Whether to create a GitHub repository and push the initial commit (requires GitHub CLI).
   Yes
🔒 Create a private GitHub repository?
   No
🔄 Whether to create a venv and sync the project after creation using uv.
   Yes

Copying from template version 2.1.0.post5.dev0+39f02f1
    create  readthedocs.yml
    create  LICENSE
    create  README.md
    create  tests
    create  tests/conftest.py
    create  tests/__init__.py
    create  tests/test_test_package.py
    create  docs
    create  docs/sphinx
    create  docs/sphinx/requirements.txt
    create  docs/sphinx/changelog.md
    create  docs/sphinx/_static
    create  docs/sphinx/_static/favicon.ico
    create  docs/sphinx/_static/sdss_logo.png
    create  docs/sphinx/_static/sdssv_logo.png
    create  docs/sphinx/_static/custom.css
    create  docs/sphinx/_static/sdssv_logo_small.png
    create  docs/sphinx/_static/favicon_sdssv.ico
    create  docs/sphinx/conf.py
    create  docs/sphinx/index.rst
    create  CHANGELOG.md
    create  .copier-answers.yml
    create  .gitignore
    create  .github
    create  .github/workflows
    create  .github/workflows/lint.yml
    create  .github/workflows/test.yml
    create  .github/workflows/release.yml
    create  post_copy.py
    create  CODEOWNERS
    create  pyproject.toml
    create  noxfile.py
    create  src
    create  src/test_package
    create  src/test_package/__init__.py

 > Running task 1 of 1: ['/Users/gallegoj/Documents/Code/sdss5/python_template/.venv/bin/python3', 'post_copy.py']
  > Parsed Copier answers file.
  > Updated LICENSE file to BSD-3-Clause.
  > Project synced with 'uv'.
  > Initialized git repository.
  > Added GitHub remote 'git@github.com:albireox/test_project.git'.
  > Staged all files for initial commit.
  > Removed copier files from staging.
  > Created initial commit.
  > Created GitHub repository.
  > Pushed initial commit to GitHub.
  > Deleted post_copy.py file.
  > Deleted .copier-answers.yml file.
```

First you will be asked for the project and package names. In general these should be the same, and it is the name of the package that you will import (e.g., `import my_package`) as well as the name of the package in PyPI once you release it. [PEP 8](https://peps.python.org/pep-0008/#package-and-module-names) defines the package name requirements, which essentially boils down to using lowercase, underscores, and no other spaces or symbols. In some special cases you may want your package name to be different from your project name. The project name is used as the repository name and in other places such as the documentation.

The template then asks for a short description for the project that will be included in the `README.md` and `pyproject.toml` files, and the name and email of the owner of the package. You will then need to select a license. SDSS uses the BSD 3-Clause license as its preferred license, but you can use a different one if appropriate. If the license you want to use is not included in the list select one of the them and then manually edit the `pyproject.toml` and `LICENSE` files in the rendered template.

The user is then asked for the GitHub namespace or organization that will host the project repository. It defaults to the [SDSS organization](https://github.com/sdss) but if you want to use your GitHub space, write your GitHub username here. You then need to provide your GitHub username. It is possible for the template to create the repository (public or private) and push the initial contents of the rendered template. This requires having the [GitHub CLI](https://cli.github.com) installed and already authenticated. Finally, the post-copy task can create a virtual environment and sync the project for you.

## Developing with your new package

Once your project directory has been rendered, the first step is to create a virtual environment to develop on. It is [essential](https://pythonforengineers.com/blog/python-tip-always-use-a-virtual-environment/index.html) that you use a virtual environment as opposed to a global Python installation. We recommend that you read the [relevant uv documentation](https://docs.astral.sh/uv/guides/projects/) for working with Python projects.

If you selected the option "Whether to create a venv and sync the project after creation using uv" during the template copy, a new virtual environment will have already been created under `<project-root>/.venv` and the dependencies will have been installed.

If you didn't select that option, you can do that manually by going to the project root and running

```bash
$ uv sync --all-groups --all-extras
Using CPython 3.14.2
Creating virtual environment at: .venv
Resolved 97 packages in 8ms
Installed 89 packages in 145ms
 + accessible-pygments==0.0.5
 + alabaster==1.0.0
 + anyio==4.12.0
 + argcomplete==3.6.3
 + asttokens==3.0.1
 + attrs==25.4.0
 + babel==2.17.0
 + beautifulsoup4==4.14.3
 ...
 + test-package==0.1.0a1 (from file:///Users/gallegoj/Downloads/test_project)
 + traitlets==5.14.3
 + typing-extensions==4.15.0
 + urllib3==2.6.2
 + uvicorn==0.40.0
 + virtualenv==20.35.4
 + watchfiles==1.1.1
 + wcwidth==0.2.14
 + websockets==15.0.1
```

This will create the `.venv` virtual environment and install all the dependencies, including development ones.

Once the virtual environment has been created there are two main ways to use it. You can activate the environment by sourcing it, e.g.,

```bash
source .venv/bin/activate
```

and then run commands normally, or you can use `uv run` and let uv ensure that you are using the package environment. For example, to run an IPython terminal with the virtual environment do

```bash
uv run ipython
```

The code for the package can be found under `src/<package-name>`. When you sync a project with uv the package is installed in "editable" mode, which means that you don't need to resync or reinstall the package when you make changes to it. The code in the package template is extremely simple, just a `__init__.py` file that provides a `__version__` variable with the version of the package, read from the `pyproject.toml` file or the package metadata.

### Adding dependencies

To add new dependencies to your package we recommend that you read [this section](https://docs.astral.sh/uv/concepts/projects/dependencies/) from the uv documentation. Modern Python package support three types of dependencies:

* Standard dependencies. These are the packages that are installed when you `pip install` your package. You can add a new dependency with `uv add <dependency>` from the root of your project, e.g., `uv add numpy`. By default, uv will install the latest version available. You can restrict this, e.g., `uv add numpy<2`. See the documentation for more details on dependency specification, including installing dependencies from a file or a remote repository.
* Optional dependencies. These are additional dependencies that you install like `pip install sdssdb[all]` and specify additional, non-default package to install. `[all]` is called an "extra". Extras can be used to customize the behaviour of your package while keeping the default dependencies limited. They can be specified with the `--optional` flag and the name of the dependency extra, e.g., `uv add httpx --optional network`.
* Development dependencies. These are dependencies that are only used for development and not included when the package is installed in production. They can only be installed when syncing with uv or other package manager that supports [PEP 735](https://peps.python.org/pep-0735/). Typical development dependencies include linters, formatters, testing tools, etc. A new development dependency can be added to a dependency "group" as `uv add --group dev ipython`. The SDSS template includes three development dependency groups by default, `dev` with linters, debuggers, etc., `test` with [pytest](https://docs.pytest.org/en/stable/) and plugins, and `docs` with [Sphinx](https://www.sphinx-doc.org/en/master/) and extensions.

You may have noticed that when we synced the project we used

```bash
uv sync --all-extras --all-groups
```

By default, `uv sync` only syncs the `dev` development group and none of the optional extras.

```{hint}
Specifying reasonable dependencies that play well with other package is not a trivial issue, and how much you need to worry about it may depend on the intended purpose of your package.

If your package is an application that is meant to run by itself (e.g., an actor or a web application) you can assume that it will be deployed in an isolated environment such as a Python virtual environment or Docker container. In that case the situation is very similar to development and you can generally choose any dependencies and version you want.

If you package is a general-use library that will be imported by other packages and needs to be installed in an environment with other dependencies, things get a bit more complicated. In this case you want to be careful when defining the minimal version of your dependencies. uv and modern versions of `pip` include good dependency resolution engines that try to solve the network of inter-related dependencies and install package versions that are valid for all specifications, but in some cases this may not be possible. For example, imagine that you require `numpy>=2.0` in your new package. Many other packages may not have migrated to Numpy 2 yet and may specify `numpy<2` in their dependecies. If you try to install your package alongside it, a dependency conflict will occur. Do you really need Numpy 2? If that is the case you may need to document this choice and be ready for potential conflicts; otherwise maybe you can relax the dependency to `numpy>=1.0` and let the dependency managers choose the best version to install.
```

### Manually editing `pyproject.toml`

You can also edit the dependencies directly in `pyproject.toml` after which you can run `uv sync` to update the environment and regenerate the `uv.lock` file. The [lock file](https://docs.astral.sh/uv/concepts/projects/layout/#the-lockfile) is a definition of the exact versions of the packages that should be installed to reproduce your current environment. Unlike the `pyproject.toml` file that defines the general requirements for your dependencies, the lock file captures the frozen state of your development process. The lock file is not included when a project is released and is only used for development. The lock file must be committed with your project.

It's beyond the scope of this documentation to describe all the options available in the `pyproject.toml` file. We refer the use to the [pyproject.toml documentation](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/). The `pyproject.toml` file is also used to include configuration for tools such as [Ruff](https://docs.astral.sh/ruff/configuration/) or pytest. It is preferred to use the `pyproject.toml` file for these configurations where possible, rather than using different files such as `ruff.toml`.

### IDE configuration

Most IDEs allow running linting and formatting when a file is saved. In Visual Studio Code we recommend installing the Python, Pylance, and Ruff extensions, and then adding this configuration to `.vscode/settings.json` at the root of your project (or select `Preference: Open Workspace Settings (JSON)` from the command panel).

```json
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": "explicit",
      "source.organizeImports.ruff": "explicit"
    },
    "editor.wordWrap": "off",
    "editor.tabSize": 4,
    "editor.defaultFormatter": "charliermarsh.ruff"
  },
  "editor.rulers": [88],
  "editor.wordWrapColumn": 88,
  "python.analysis.typeCheckingMode": "basic",
}
```

## Template features

### Package testing

The SDSS template includes a stub for unit-testing using [pytest](https://docs.pytest.org/en/stable/). The test files are located at the root of the rendered project under `tests/`. A basic test is included that checks that the package can be imported and its version read. The tests can be run with

```bash
$ uv run pytest
Test session starts (platform: darwin, Python 3.14.2, pytest 9.0.2, pytest-sugar 1.1.1)
rootdir: /Users/gallegoj/Downloads/test_project
configfile: pyproject.toml
plugins: mock-3.15.1, anyio-4.12.0, asyncio-1.3.0, sugar-1.1.1, cov-7.0.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1 item

 tests/test_test_package.py ✓                                                                  100% ██████████

Results (0.35s):
       1 passed
```

Fixtures and other pytest features can be defined in the `tests/conftest.py` file.

### Package documentation

A stub for [Sphinx documentation](https://www.sphinx-doc.org/en/master/) can be found under `docs/sphinx`. The documentation uses the [furo](https://github.com/pradyunsg/furo) theme. The documentation can be configured by editing the `docs/sphinx/conf.py` file.

A helper script is provided to render the documentation, open it in a browser, and watch for file changes. From the root of the project run

```bash
nox
```

and wait until a new browser window is open. You can then edit files under `docs/sphinx` and the documentation will reload when you save them.

The [MyST](https://myst-parser.readthedocs.io/en/latest/index.html) extension is included, which allows writing documentation using Markdown files in addition to reStructuredText.

The template provides a `readthedocs.yml` file that should make deploying to [ReadTheDocs](https://about.readthedocs.com) trivial. Just go to your RTD dashboard and add the project. Please make sure you then go to the settings of the RTD project and, under Maintainers, you add the `sdss` account. This will allow other people manage the RTD documentation if you stop maintaining the project. You can also ask an SDSS maintainer to enable the RTD documentation for you using the `sdss` account.

Due to limitations in how RTD can install projects, the documentation dependencies are specified in two places: in `pyproject.toml` under the `docs` development group, and in `docs/sphinx/requirements.txt`. The former is used for local development; the latter are installed when the project is built in RTD. If you need to add a new dependency or Sphinx extension, make sure that you add it in both places.

### Linting and formatting

The template uses [Ruff](https://docs.astral.sh/ruff) to enforce linting and formatting according to the [SDSS style standards](style/STYLE_v2). The configuration is fairly vanilla and can be found in the `pyproject.toml` file. A few rules are bypassed but for the most part the standard Ruff configuration and rules are used. Import sorting includes a special group for SDSS tools such as [sdsstools](https://github.com/sdss/sdsstools) or [sdssdb](https://github.com/sdss/sdssdb).

Linting can be checked by running

```bash
$ uv run ruff check src tests
All checks passed!
```

and formatting can be checked with

```bash
$ uv run ruff format --check src tests
4 files already formatted
```

Remove the `--check` to allow Ruff formatting the files in place.

Again, we recommend using linting and formatting directly with your IDE of choice.

### Continuous Integration (CI)

The template includes three [GitHub Actions workflows](https://docs.github.com/en/actions) under `.github/workflows`:

* `lint.yml` runs a linting and format check using Ruff every time a commit is pushed to the repository. The files are not modified.
* `test.yml` runs the pytest tests using different Python versions under Linux (Ubuntu 24.04). This workflow also runs on each commit.
* `release.yml` runs when a new tag is pushed and creates a new GitHub release using the contents of the `CHANGELOG.md` file. The package is built and published to PyPI (see [Publishing your package](#publishing-your-package) below).

The `test.yml` action outputs information about test coverage, but that information is not uploaded to any service by default. We recommend using [codecov](https://about.codecov.io) for this. To enable uploading coverage reports you will need to log in to your codecov account, select the project in question, go to Configuration — General and copy the `CODECOV_TOKEN` value. Then go to your project page in GitHub, access the Settings, Secrets and variables, Actions, and add a new Repository secret with name `CODECOV_TOKEN` and value the copied token. Then edit `.github/workflows/test.yml` and uncomment the "Upload coverage to Codecov" section.

## Publishing your package

Distributing a package involves two steps: "building" your package, and "publishing" it.

Building means packaging your code in a single file that can be used to install it in a different machine. Python supports two types of distributions: source files which are just tarballs with your code plus metadata files needed to install it (essentially the same as cloning the repository and installing it, but in a single file and including only the absolutely necessary files); and "wheels", which are binary distributions including extensions and other architecture-dependent files.

Building the source and wheel files for a given Python version and architecture is easy, and you can do it by running

```bash
uv build
```

this will create two files in `dist/`, one with `.tar.gz` with the source distribution and a `.whl` wheel.

The next step is to publish these files to an online service that allows other users to download and install it. Although there are other options, almost every Python package is published to the [PyPI registry](https://pypi.org). PyPI requires you to have an account and generate a token to upload files. Then you can generate a token and upload the distribution files using uv,

```bash
uv publish
```

See the [uv documentation](https://docs.astral.sh/uv/guides/package/#publishing-your-package) about how to authenticate uv with PyPI.

Alternatively, the `release.yml` GitHub Action will do this for you every time you tag and release a new version. PyPI requires defining a [trusted publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/) to allow CI services uploading files to PyPI. If you have not yet published your package to PyPI you will also want to [read this page](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/) to create a trusted published for a not-yet-existing project.

### Keeping a changelog

Keeping a log of the changes to your project is critical. Refer to the [coding standards](style/STYLE_v2) for details on the preferred format. Before releasing a new version make sure that you update the `CHANGELOG.md` file with the changes and that they are listed under a heading with the tag name. The `release.yml` workflow uses [taiki-e/create-gh-release-action](https://github.com/taiki-e/create-gh-release-action) to capture the changelog content for the new version and include it in the GitHub release.

### Workflow for releasing a new version

As you develop your package you will settle on a workflow that works for you. That said, here is a workflow that usually works well:

* Work on the `main` branch. Try to make small, atomic commits that fully implement a feature or bug fix. Depending on the project and severity of the changes, you can work and commit directly on `main`. For larger changes or projects with multiple developers, create a new branch, make changes there, open a new pull request and merge (after appropriate code review) to `main`. For very large projects consider using forks.
* As you commit changes, edit the `CHANGELOG.md` file. Include not-yet-relesed changes under a `Next release` heading, sorted in categories (Breaking changes, New features, Bug fixes, Improvements, etc.)
* When you are ready to release a new version run `uv version <new version>`, e.g., `uv version 1.2.3`. Edit the `CHANGELOG.md` file and rename `Next release` to  the version and date (`1.2.3 - 2025-12-15`). Commit the changes with the commit message `"Release 1.2.3"`. Tag a new version with `git tag -a 1.2.3 -m "<project-name> 1.2.3"`. Push changes with `git push` and `git push --tags`.
* Confirm on GitHub that the release workflow run successfully, created the new GitHub release with the CHANGELOG contents, and that the new files were uploaded to PyPI.
* Bump the version back to pre-release, `uv version 1.2.4a1`. Commit the changes with message `"Bump version to 1.2.4a1"`.
* Continue developing against the `main` branch.

## Updating a project that uses this template

The SDSS template is actively maintained with bug fixes and new features. You can update an existing project generated from the template to incorporate these improvements. To enable updates, you must preserve the `.copier-answers.yml` file when initially generating your project. This file tracks your project's relationship to the upstream template and should not be manually edited.

To update your project, go to the root of the local checkout, ensure that there are no uncommitted changes (either commit or stash them), and run

```console
$ uvx copier update --skip-tasks --skip-answered --trust
Updating to template version 2.1.0.post27.dev0+5b8f556
```

After the update you may have one or more file that have been updated. Those will show up if you do a `git status`. The update will never commit any changes, so you can always revert or discard the update.

It is possible for the updates to conflict with your own changes (for example if you have manually edited the GitHub workflows). Carefully review any changes and solve conflicts before you commit the new files.

## Building and publishing a Docker image

During the project generation process you will be asked if you want to include a `Dockerfile` and workflow for build a Docker image. If you select "Yes", a `Dockerfile` will be added to your project and the `docker.yml` GitHub Action workflow will run on each push and tag. The action will build the image and upload it to the [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) under the `ghcr.io` namespace. The resulting image will be automatically associated with your repository (you can find it on the right sidebar under "Packages"). You can then pull the image with

```bash
docker pull ghcr.io/<github-organization>/<project-name>:latest
```

Note that the included `Dockerfile` is very basic and does not include an entry point. You will need to edit it to suit your needs. We recommend checking the [uv Docker documentation](https://docs.astral.sh/uv/guides/integration/docker/) to learn how to work with the uv base images.

## Advanced topics

### Updating the package version

Updating the package version can be done directly in the `pyproject.toml` file by modifying the `version` entry and then running `uv sync` to update the lock file. [Alternatively](https://docs.astral.sh/uv/guides/package/#updating-your-version) one can use `uv version <new-version>`.

### Build backend and extension modules

By default, the template uses the [uv build backend](https://docs.astral.sh/uv/concepts/build-backend/) which will be used to build and publish the package under `src/`. The build backend will include all Python files and other files in the `src/<package-name>` directory, while removing cache and temporary files and including metadata files such as `pyproject.toml`, the README file, and the license. Including/excluding other files is not always trivial. Read the [relevant section](https://docs.astral.sh/uv/concepts/build-backend/#file-inclusion-and-exclusion) if you need to do that.

The uv backend is enough for most purposes. One case where that is not the case is when the package must include compiled extension modules (e.g., a C/C++ library that is compiled when the package is built). The uv backend does not support extensions and a different backend, such as [scikit-build-core](https://github.com/scikit-build/scikit-build-core) or [setuptools](https://setuptools.pypa.io/en/latest/userguide/ext_modules.html) must be used. See the [uv documentation](https://setuptools.pypa.io/en/latest/userguide/ext_modules.html) for more details. The [flicamera](https://github.com/sdss) is an example of a tool using `pyproject.toml` and uv with a `setuptools` build backend (see the `pyproject.toml` and `setup.py` files).

### Scripts and command line tools

Python packaging supports defining scripts and command line interfaces under the general term of [entry points](https://packaging.python.org/en/latest/specifications/entry-points/), which can be defined in the `pyproject.toml` file. The SDSS template does not include any entry points by default, but you can easily add them by editing the `pyproject.toml` file. See the [relevant documentation](https://docs.astral.sh/uv/concepts/projects/config/#entry-points) in uv for details and examples.

The specification only allows running Python functions as scripts. The script definition is the path to the function to run. For example, we can define the following function that prints the version of our package:

```{code-block} python
:caption: src/my_package/cli.py

from my_package import __version__

def print_version():
   print(f"The package version is {__version__}.")

```

And then add the following lines in `pyproject.toml`:

```{code-block} toml
:caption: pyproject.toml

[project.scripts]
my-package-version = "my_package.cli:print_version"
```

After syncing the project again we can do

```bash
$ my-package-version
0.1.0a1
```

You can use this as an entry point for a fully-featured command line interface using packages such as [Click](https://click.palletsprojects.com/) or [Typer](https://typer.tiangolo.com/).

If you need to run a non-Python script, you can include it in your `src/<package-name>` directory, for example under `scripts/`, and then include a Python entry point that runs that script using `subprocess.run()`.

```{code-block} bash
:caption: src/my_package/scripts/myscript.sh
#!/bin/bash
echo "Hello from myscript.sh"
```

```{code-block} toml
:caption: pyproject.toml
[project.scripts]
my-script = "my_package.__main__:run_myscript"
```

```{code-block} python
:caption: src/my_package/__main__.py
import pathlib
import subprocess

def run_myscript():
    cwd = pathlib.Path(__file__).parent
    subprocess.run(["bash", str(cwd / "scripts/myscript.sh")])
```

Finally, you can use external tools to run development scripts and to automate certain tasks. One such option is [poe](https://poethepoet.natn.io/global_options.html), which integrates well with uv and `pyproject.toml`. For example, you can define a `poe` task to run the tests as

```{code-block} toml
:caption: pyproject.toml
[tool.poe.tasks]
test-coverage = "pytest tests/"
```

Add `poethepoet` to the `dev` development group as `uv add --group dev poethepoet` and then you can run

```bash
$ poe test
Poe => pytest --cov=test_package tests/
      Built test-package @ file:///Users/gallegoj/Downloads/test_project
Uninstalled 1 package in 0.76ms
Installed 1 package in 1ms
Test session starts (platform: darwin, Python 3.14.2, pytest 9.0.2, pytest-sugar 1.1.1)
rootdir: /Users/gallegoj/Downloads/test_project
configfile: pyproject.toml
plugins: mock-3.15.1, asyncio-1.3.0, sugar-1.1.1, cov-7.0.0
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 1 item

 tests/test_test_package.py ✓                                                                                                                     100% ██████████
======================================================================== tests coverage =========================================================================
_______________________________________________________ coverage: platform darwin, python 3.14.2-final-0 ________________________________________________________

Name                           Stmts   Miss  Cover
--------------------------------------------------
src/test_package/__init__.py       4      0   100%
src/test_package/__main__.py       5      5     0%
--------------------------------------------------
TOTAL                              9      5    44%

Results (0.08s):
       1 passed
```

### Multi-architecture distributions

As discussed above, running `uv build` will create wheels only for the current architecture. This is usually fine since Python code is interpreted and multi-platform. But if you code include compiled extensions or scripts (C/C++, Rust), the wheels will only work for the native architecture. This means that if a user tries to install your package in a different platform, they will instead download the source distribution and compile it. Again, this is usually fine but slower, and requires the user to have the tools to compile your extension (usually a GCC compiler and the appropriate libraries).

Instead, it is possible to use CI to generate wheels for a variety of architectures. It's beyond the scope of this guide to describe the process in detail, but you can either create a matrix of CI workers with different architectures and Python versions, save the wheels as artifacts and upload them to PyPI, or use a tool such as [cibuildwheel](https://cibuildwheel.pypa.io/en/stable/) to automate the process. You can check [this workflow](https://github.com/sdss/sdss-sep/blob/c55b6b3e8b6117b4d47bd921d8e983c4a2234eea/.github/workflows/build-wheels-upload-pypi.yml) for a working example.

### What if I really don't want to use uv?

uv is quickly becoming the standard for Python packaging, but if you prefer to use a different package manager (or no manager at all), it's easy to modify the template to do so. Except for the dependency groups, nothing in the `pyproject.toml` or other files is specific to uv (and the dependency groups are understood by any dependency manager that supports [PEP 735](https://peps.python.org/pep-0735/)). The only thing you'll need to do is to replace the `[build-system]` section in `pyproject.toml` with your build system if choice. If you want an experience as similar as possible to old-style Python packaging, use the `setuptools` build system

```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```

and check the [documentation](https://setuptools.pypa.io/en/latest/userguide/index.html).

## Changelog

The change log for the SDSS Python Template can be found
[here](changelog.md).

## Links

* [Repository](https://github.com/sdss/python_template)
* [Issue tracking](https://github.com/sdss/python_template/issues)
