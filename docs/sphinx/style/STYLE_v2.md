# SDSS coding standards

```{warning}
This is the current version of the SDSS coding standards. For the previous version, see [STYLE_v1](STYLE_v1).
```

This document outlines the coding standards that all SDSS and SDSS-affiliated software must follow. These standards are intended to make sure that the code adheres to modern coding practices, is easy to maintain, and is usable by the entire collaboration. Deviations from this standard, where reasonable, must be decided by the repository owner(s) and documented in the repository README. Where possible, please provide linter configuration files to enforce those departures from the standard.

## Languages

SDSS does not enforce a specific coding language. However, Python 3.10+ is strongly preferred due to its prevalence in the astronomical community. *Do not* develop new Python 2 code; maintain existing Python 2 repositories only if migration to Python 3 is not feasible.

Where necessary, Python code can be extended with C/C++ or other compiled languages. When distributing code with compiled extensions, provide prebuilt binaries for a reasonable range of architectures and operating systems to reduce friction for users who lack a build environment.

## Code storage and ownership

All code must be version-controlled using [git](https://git-scm.com/).

All code must live in the [SDSS GitHub organisation](https://www.github.com/sdss). Code that is specific to Apache Point Observatory and is shared with other on-site telescopes should be put in [their own](https://github.com/ApachePointObservatory) organization. When starting a new product, start a new repository in the GitHub organization (public or private) and follow the instructions to clone it to your computer. Feel free to create forks of the repositories to your own GitHub account, but make sure the production version of the code lives in the organization repo.

If your code is already in GitHub, move it to the SDSS GitHub organization as soon as it is ready to be shared. This can be done easily by creating a new repository in the SDSS GitHub, adding it as a new remote to your local checkout, and pushing to the new remote.

All code must have *at least* one owner, who is ultimately responsible for keeping the code working and making editorial decisions. Owners can make decisions on which code standards to follow (within the requirements listed in this document), such as maximum line length, linter, or testing framework. The owner(s) names should be obvious in the README of the repo and in the ``pyproject.toml`` file (for Python projects). A [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) file can be used (and it is included with the template) to record code ownership in a machine-readable manner.

## Tagging, versioning, and change logs

**All production software must run from tagged versions.** The only exception to this rule is when debugging new code during engineering or test runs.

Following [PEP 440](https://www.python.org/dev/peps/pep-0440/), software versions should use the convention ``X.Y.Z`` (e.g., ``1.2.5``) where X indicates the major version (large, maybe non-backwards compatible changes), Y is for minor changes and additions (backwards compatible), and Z is for bug fixes (no added functionality). Suffixes to the version, such as ``dev``, ``alpha``, and ``beta``, are accepted. Do not use a hyphen between version and suffix (``1.2.5dev`` is ok, ``1.2.5-dev`` is not). Note that PEP 440 recommends separating suffixes with a period (``1.2.5.dev``) but we have found that sometimes causes problems with pip.

For products that already have tagged versions using the old SDSS versioning standards (e.g., ``v1_2_3``), tag new versions using the new convention (e.g., ``1.2.4``) but do not rename or retag previous versions.

Python packages must return their version via the ``__version__`` attribute. All other products, including metadata and datamodels, must also be versioned in a clear and obvious way. When tagging using git, prefer [annotated tags](https://git-scm.com/docs/git-tag).

The value of the `__version__` attribute in Python projects should not be hardcoded. Instead, it must be calculated from the [module metadata](https://docs.python.org/3/library/importlib.metadata.html). The [sdsstools](https://github.com/sdss/sdsstools) `get_package_version` can be used for this purpose. In the package top-level `__init__.py` file, add:

```python
from sdsstools import get_package_version

NAME = "sdssdb"  # The package name (this is the pip-install name)

__version__ = get_package_version(path=__file__, package_name=NAME)
```

All changes should be logged in a ``CHANGELOG.md`` or ``CHANGELOG.rst`` file. The change log should be structured in different sections (Breaking changes, New, Improved, ...). Before tagging, add a heading indicting the version and tag date. Untagged changes should be recorded under a "Next release" heading. See [the template CHANGELOG.md](../changelog.md) for an example of formatting. When releasing a new version, copy the change log for the relevant version in the GitHub release description.

## Deployment

SDSS Python packages should follow general Python packaging standards. For documentation, [start here](https://packaging.python.org/).

Store package metadata and dependencies in a [pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) file that follows [PEP 621](https://peps.python.org/pep-0621/). Include a `build-system` section specifying the build backend (see [PEP 517](https://peps.python.org/pep-0517/)).

Should you deploy to PyPI? Generally yes, but consider your project's scope. If your code targets mountain operations and requires module/EUPS version control, PyPI deployment may be unnecessary. However, if your product will be widely distributed within the collaboration (analysis tools, pipelines, schedulers), you **must** publish to PyPI. Tools like [uv](https://docs.astral.sh/uv) or [poetry](https://python-poetry.org) simplify building and publishing. Alternatively, manually build source and wheel files and upload them with [twine](https://github.com/pypa/twine). Regardless of PyPI deployment, **all code must be properly packaged and installable via pip**.

SDSS maintains a [PyPI account](https://pypi.org/user/sdss/) whose credentials are available from ``admin[at]sdss[dot]org``. You may use your own account, but ensure ``sdss`` is listed as an **owner** of all SDSS software.

## Open-source code and licensing

SDSS code is distributed as open-source under a [BSD 3-Clause licence](https://opensource.org/license/bsd-3-clause) by default. Other open-source licences may be used if appropriate and after discussion with other members of the collaboration. Closed code and private repositories should be restricted to code that could expose secrets or make collaboration services vulnerable.

## Coding style

SDSS code follows the [PEP8 standard](https://www.python.org/dev/peps/pep-0008/). Please read that document carefully and follow every convention, unless there are very good reasons not to.

It is beyond the scope of this document to summarise the PEP8 conventions, but here are some of the most salient points:

- Indentation of four spaces. **No tabs. Ever.**
- Two blank lines between functions and classes. One blank line between methods in a class. A single line at the end of each file.
- Always use spaces around operators and assignments (``a = 1``). The only exception is for function and method keyword arguments (``my_function(1, key='a')``).
- No trailing spaces. You can configure your editor to strip the lines automatically for you.
- Imports go on the top of the file. Do **not** import more than one package in the same line (``import os, sys``). Maintain the namespace, do **not** import all functions in a package (``from os import *``). You can import multiple functions from the same package at the same time (``from os.path import dirname, basename``). Imports should be sorted following a clear convention for the package.
- Use single quotes for strings. Double quotes must be reserved for docstrings and string blocks.
- For inline comments, at least two spaces between the statement and the beginning of the comment (``a = 1  # This is a comment about a``).
- Class names must be in camelcase (``class MyClass``). Function, method, and variable names should be all lowercase separated by underscores for legibility (``def a_function_that_does_something``, ``my_variable = 1``). For the latter ones, PEP8 allows some flexibility. The general rule of thumb is to make your function, method, and variable names descriptive and readable (avoid multiple words in all lowercase). As such, if you prefer to use camelcase (``aFunctionThatDoesSomething``, ``myVariable = 1``) for your project that is accepted, as long as you are consistent throughout the project. When modifying somebody else's code, stick to their naming decisions.
- Use ``is`` for comparisons with ``None``, ``True``, or ``False``: ``if foo is not None:``.

### Docstrings

Docstrings are special comments, wrapped between two sets of three double quotes (``"""``). Their purpose is dual: they provide clear, well structured documentation for each class and function in your code, and they are intended to be read by an automatic documentation generator (see the [Automatic documentation generation](#automatic-documentation-generation) section). For docstrings, follow [PEP257](https://www.python.org/dev/peps/pep-0257/). In our template, ``main.py`` contains some examples of functions and classes with docstrings; use those as an example. In general:

- **All** code should be commented. **All** functions, classes, and methods should have a docstring.
- Use double quotes for docstrings; reserve single quotes for normal strings.
- Limit your docstrings lines to 72 characters. This convention can be a bit constraining for some developers; it is OK to ignore it and use the line length you are using for your code (79 or 99 characters).
- A complete docstring should start with a single line describing the general purpose of the function or class. Then a blank line and an in-depth description of the function or class in one or more paragraphs. A list of the input parameters (arguments and keywords) follows, and a description of the values returned, if any. If the class or function merits it, you should include an example of use.
- The docstring for the ``__init__()`` method in a class goes just after the declaration of the class and it explains the general use for the class, in addition to the list of parameters accepted by ``__init__()``.
- Private methods and functions (those that start with an underscore) may not have a docstring **only** if their purpose is really obvious.
- In general, we prefer [Google style](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html#example-google) docstrings over [Numpy style](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy) ones, but you are free to choose one as long as you stick with it across all the product. Avoid styles such as ``param path: The path of the file to wrap`` which are difficult to read.

### Linters and formatters

**Do use a linter.** These are plugins available for almost every editor (Visual Studio Code, vim, Emacs, Sublime Text, Atom) that run every time you save your code and show syntax errors and where you are not following PEP8 conventions.

We strongly suggest using [Ruff](https://docs.astral.sh/ruff), which has become the de facto standard for Python linting. The SDSS Python templates includes a Ruff configuration that is compliant with the specifications described above. Ruff can also be used to format your code so that it meets the linting requirements.

The following `pyproject.toml` configuration can be used:

```toml
[tool.ruff]
line-length = 88
target-version = 'py313'

[tool.ruff.lint]
select = ["E", "F", "I"]
unfixable = ["F841"]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F403", "E402", "F401"]

[tool.ruff.lint.isort]
known-first-party = ["my_package"]
lines-after-imports = 2
section-order = ["future", "standard-library", "typing", "third-party", "sdss", "first-party", "local-folder"]

[tool.ruff.lint.isort.sections]
typing = ["typing"]
sdss = ["sdsstools", "sdssdb", "clu", "tree", "sdss_access", "datamodel", "coordio"]
```

### File headers

Include a header in each Python file describing the author, license, etc. We suggest:

```python
# encoding: utf-8
#
# @Author:
# @Date:
# @Filename:
# @License:
# @Copyright:

from __future__ import annotations
```

In general, do not include comments about when you last modified the file since those become out of date really fast. Instead, use a [CHANGELOG file](#tagging-versioning-and-change-logs) and atomic git commits.

Non-Python executable scripts can be stored under a ``bin/`` directory. For those files, add an appropriate shebang at the beginning of the header, for example:

```bash
#!/usr/bin/env python
```

### General advice

- Blank lines only add one byte to your file size; use them prolifically to improve legibility.
- Read the [Zen of Python](https://www.python.org/dev/peps/pep-0020/). Explicit is better than implicit. Simple is better than complex.
- Know when ignore these standards if there is a good reason, or it improves readability (but don't use that as an excuse to just not follow the standards).

## Testing

Do test your code. Do test your code. Do test your code. As the repository owner, you are ultimately responsible for ensuring the software behaves as intended and that new features do not break existing functionality.

Modern testing should focus on two pillars: unit testing and continuous integration (CI).

- Unit testing verifies small, isolated parts of the code with fast, deterministic tests. Add tests for every new feature and bug fix, and strive for meaningful coverage.
- CI runs the test suite automatically on each commit and pull request across supported environments, preventing merges when tests fail and reporting coverage.

### Unit testing

Unit testing advocates for breaking your code into small "units" that you can write tests for (and then actually write the tests!). There are multiple tutorials and manuals online; [this one](http://docs.python-guide.org/en/latest/writing/tests/) is a good starting point.

Many libraries and frameworks for testing exist for Python. The basic (but powerful) one is called [unittest](https://docs.python.org/3/library/unittest.html) and is a standard Python library. [pytest](https://docs.pytest.org/en/latest/) includes a number of extremely convenient and powerful features, as well as many third-party addons. Features such as [parametrising tests](https://docs.pytest.org/en/latest/parametrize.html#pytest-mark-parametrize-parametrizing-test-functions) and [fixtures](https://docs.pytest.org/en/latest/fixture.html) are excellent to make sure your code gets a wide test coverage. This template includes a simple pytest setup. You can also look at the [Marvin test suite](https://github.com/sdss/marvin/tree/master/python/marvin/tests) for a more complete example.

### Code coverage

We recommend utilizing code coverage tools to assess the extent of code execution and testing achieved by your unit tests. The `pytest` framework supports generating coverage reports through the [pytest-cov](https://github.com/pytest-dev/pytest-cov) extension, which is already configured in the SDSS template. Alternatively, the [coverage](https://coverage.readthedocs.io/en/) package can also be employed. These tools produce coverage reports in various formats, including HTML for user-friendly viewing and machine-readable formats that can be uploaded to online services like [Codecov](https://about.codecov.io) for comprehensive coverage tracking and advanced visualizations.

## Continuous integration

It is critical that you not only write tests but run them, and do so in a suite of environments (different OS, Python versions, etc.). The preferred SDSS CI infrastructure is to use [GitHub Actions](https://github.com/features/actions) to co-locate code and CI results in the same service. GitHub Actions are defined via [workflows](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows) files that must live in the `.github/workflows/` directory at the root of your repository.

The SDSS Python template includes several workflows to help with testing, linting, and releasing.

## Automatic documentation generation

As a software developer, it is part of your responsibility to document your code and keep that documentation up to date. Documentation takes two forms: inline documentation in the form of comments and docstrings, and explicit documentation, tutorials, plain-text explanations, etc.

Explicit documentation can take many forms (PDFs, wiki pages, plain text files) but the rule of thumb is that the best place to keep your documentation is the product itself. That makes sure a user knows where to look for the documentation, and keeps it under version control.

SDSS uses and strongly encourages [Sphinx](http://www.sphinx-doc.org/en/stable/intro.html) to automatically generate documentation. Sphinx translates [reStructuredText](http://docutils.sourceforge.net/rst.html) source files to HTML (plugins for Latex, HTML, and others are available). It also automates the process of gathering the docstrings in your code and generating nicely formatted HTML code.

It is beyond the purpose of this document to explain how to use Sphinx, but [its documentation](http://www.sphinx-doc.org/en/stable/contents.html) is quite good and multiple tutorials exist online. A large ecosystem of plugins and extensions exist to perform almost any imaginable task. This template includes a basic but functional [Sphinx template](<../index.md#package-documentation>).

### Read the Docs

Deploying your Sphinx documentation is critical. SDSS uses [Read the Docs](https://readthedocs.org) to automatically build and deploy documentation. Read the Docs can be added as a plugin to your GitHub repo for continuous integration so that documentation is built on each commit. SDSS owns a Read the Docs account. Contact ``admin[at]sdss[dot]org`` to deploy your documentation there. Alternatively, you can deploy your product in your own Read the Docs account and add the user ``sdss`` as a maintainer from the admin menu.

## Git workflow

Working with Git and GitHub provides a series of extremely useful tools to write code collaboratively. Atlassian provides a [good tutorial](https://www.atlassian.com/git/tutorials/syncing) on Git workflows. While the topic is extensive, here is a simplified version of a typical Git workflow you should follow:

1. [Clone](https://git-scm.com/docs/git-clone) the repository.
2. Create a [branch](https://git-scm.com/docs/git-branch) (usually from main) to work on a bug fix or new feature. Develop all your work in that branch. Commit frequently and modularly. Add tests.
3. Once your branch is ready and well tested, and you are ready to integrate your changes, you have two options:
    1. If you are the owner of the repo and no other people are contributing code at the time (or your changes are **very** small and non-controversial) you can simply [merge](https://git-scm.com/docs/git-merge) the branch back into main and push it to the upstream repo.
    2. If several people are collaborating in a project, you *want* to create a [pull request](https://help.github.com/articles/about-pull-requests/) for that branch. The change can then be discussed, changes made and, when approved, you can merge the pull request.
4. Repeat from step 2.

You may want to consider using [forks](https://help.github.com/articles/fork-a-repo/) if you are planning on doing a large-scope change to the code.

When merging a pull request, we recommend using [squash merges](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-request-merges#squash-and-merge-your-pull-request-commits). This collapses your pull request into a single commit, preventing you from cluttering the git history with multiple commits in the form ``test1``, ``test2``, ``another test``, etc. Note that although the commits are squashed, the full commit history of a pull request can be recovered if needed.

## Docker images

Docker images of SDSS products should be stored as [GitHub packages](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-docker-registry) within the SDSS GitHub organization and associated with the appropriate repository. This allows for easy versioning and distribution of Docker images alongside the source code. Ensure that each Docker image is tagged with the corresponding software version to maintain consistency between the codebase and its containerized environment. The template documentation contains [information](../index.md#building-and-publishing-a-docker-image) on how to set up GitHub Actions to build and deploy Docker images automatically.

## Software citation

All software should be archived and citable in some way by anyone who uses it. The AAS now has a policy for [software citation](http://journals.aas.org/policy/software.html) that SDSS should adopt for all pieces of code it produces. This policy should be adopted by internal SDSS collaborators as well as astronomers outside SDSS using SDSS software.

### Zenodo

Zenodo allows you to generate a unique digital object identifier (DOI) for any piece of software code in a GitHub repository. DOIs are citable snippets, and allow your software code to be identified by tools. See [Making Your Code Citable](https://guides.github.com/activities/citable-code/) for how to connect your GitHub repository to Zenodo. Once your GitHub repo is connected to Zenodo, every new GitHub tag or release gets a new DOI from Zenodo. Zenodo provides citable formats for multiple journals as well as export to a BibTeX file.

### Astrophysical Source Code Library

The [ASCL](http://ascl.net/) is a registry of open-source astronomy software, indexed by the [SAO/NASA Astrophysics Data System](http://ads.harvard.edu/) (ADS). The process for submission to the ASCL is outlined [here](http://ascl.net/submissions).

## Further reading

- Python's own [documentation style guide](https://devguide.python.org/documentation/style-guide/) is a good resource to learn to write good documentation.
- Astropy's [coding standards](http://docs.astropy.org/en/stable/development/codeguide.html) and [documentation guide](http://docs.astropy.org/en/stable/development/docguide.html) are good resources.
- Packaging using [setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html).
