# SDSS Python template and coding standards

**Important: this is a pre-alpha version of this document. Please, look throughout the text and at the end of the document for a list of TODO/missing parts.**

So you want to write some Python code. Congratulations, you've gotten to the right place! This repository has a dual purpose: it provides a template for a basic, but complete, Python package, and includes the coding standards and recommendations for developing code for SDSS. Please, read this document carefully. If you decide to develop your product based on this template, feel free to replace the `README.md` with a description of your project, but keep the `STYLE.md` file as a reminder of the coding conventions.

While this document deals with Python product, and some of the solutions and services suggested are specific for it, much of what is written here is general good advice for developing software in any platform.

## Python 2 vs Python 3: which one to choose?

SDSS has made the decision to transition to Python 3 by 2020. That means that all new code must *at least* be compatible with Python 3. There is, however, a very significant amount of ancillary code that is still Python 2-only and that will not be ported to Python 3 for some time.

When deciding what version of Python to write your code on, consider what are its dependencies:

- If your code is standalone, or depends on Python 3-compatible code, write it in Python 3. **You don't need to make sure your code is Python 2-backwards compatible.**

- If your code depends on key packages that are Python 2-only (e.g., `actorcore`, `opscore`, `RO`, `twistedActor`), write your code in Python 2 **but** try to make it as much Python 3-ready as possible, so that when those dependencies are upgraded you can upgrade your code easily.

Whenever you create a new Python file, make sure to add the following lines on the top of the file

```python
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
```

That will force you to use `import`, `print`, and division in a way that is Python 2 and 3-compatible.

Some resources that can be useful to write code that is Python 2 and 3-compatible, and to port code from 2 to 3:

- A [cheat sheet](http://python-future.org/compatible_idioms.html) with advice to write code compatible with Python 2 and 3.
- The [six](https://pythonhosted.org/six/#) library provides functions to write code that will work in Python 2 and 3.
- If converting code from Python 2 to 3, consider using [2to3](https://docs.python.org/2/library/2to3.html) as the starting point. It works very well for most files, and even for those files that require manual interaction, it paves most of the way.


## Code storage, versioning, and change logs.

All code must be version controlled using [git](https://git-scm.com/). Older code, still under the SVN repository, can be maintained using Subversion until it has been ported to Git.

All code must live in the [SDSS GitHub organisation](https://www.github.com/sdss). When starting a new product, start a new repository in the GitHub organisation (you can choose to make it public or private) and follow the instructions to clone it to your computer. Feel free to create forks of the repositories to your own GitHub account, but make sure the production version of the code lives in the organisation repo.

Software versions should follow the convention `X.Y.Z` (e.g., `1.2.5`) where X indicates the major version (large, maybe non-backwards compatible changes), Y is for minor changes and additions (backwards compatible), and Z is for bug fixes (no added functionality). Suffixes to the version, such as `dev`, `alpha`, `beta`, are accepted. Do not use a hyphen between version and suffix (`1.2.5dev` is ok, `1.2.5-dev` is not).

Version tracking may be complicated so we recommend using `bumpversion` (see [here](https://github.com/peritus/bumpversion) for documentation). This template already implements a [configuration file](./.bumpversion.cfg) that automates updating the version number in all the places in the code where it appears. Let's say that your current version is `0.5.1` and you are going to work on minor changes to a product. You can go to the root of the package and run `bumpversion minor`. This will update the version to `0.6.0dev` everywhere needed and commit the changes. When you are ready to release, you can do `bumpversion release` to change the version to `0.6.0`.

All changes should be logged in a `CHANGELOG.rst` or `CHANGELOG.md` file. See [the template CHANGELOG.rst](./CHANGELOG.rst) for an example of formatting. When releasing a new version, copy the change log for the relevant version in the GitHub release description.


## Deployment

SDSS Python packages should follow the general Python standards for packaging. If looking for documentation, [start here](https://packaging.python.org/).

All packages must contains a (setup.py)[./setup.py] to automate building, installation, and packaging. The `setup.py` file must take care of compiling and linking all external code (e.g., C libraries) that is used by the project.

Dependencies must be maintained in two different locations. For standard, pip-installable dependencies, use the [requirements.txt](./requirements.txt) file. See [here](https://pip.pypa.io/en/stable/user_guide/#requirements-files) for more information on using requirements.txt files. Consider using multiple requirements.txt files (e.g, `requirements.txt`, `requirements_dev.txt`, `requirements_docs.txt`) for different pieces of functionality. Additionally you must maintain the [module](etc/python_template.module) file for your product. If you package depends on SDSS-specific, non pip-installable packages, use the module file to load the necessary dependencies.

Should you make your package pip-installable? The general answers is yes, but consider the scope of your project. If your code is to be used for mountain operations and needs to be maintained with modules/EUPS version control, making it pip installable may not be necessary, since it is unlikely to be installed in that way. However, if your product will be distributed and installed widely in the collaboration (examples of this include analysis tools, pipelines, schedulers), you *must* make it pip-installable. Start [here](https://pip.pypa.io/en/stable/) for some documentation on making pip-installable packages. Another good resource is [twine](https://github.com/pypa/twine), which will help you automate much of the packaging and uploading process.

SDSS has a [PyPI account](https://pypi.org/user/sdss/) that should be used to host released version of your pip-installable projects. Do not deploy the project in your own account. Instead, contact [XXX](mailto:me@email.com) to get access to the PyPI account.


## Coding style

SDSS code follows the [PEP8 standard](https://www.python.org/dev/peps/pep-0008/). Please, read that document carefully and follow at every, unless there are very good reasons not to.

The only point in which SDSS slightly diverges from PEP8 is the line length. While the suggested PEP8 maximum line length of 79 characters is recommended, lines up to 99 characters are accepted. When deciding what line length to use follow this rule: if you are modifying code that is not nominally owned by you, respect the line length employed by the owner of the product; if you are creating a new product that you will own, feel free to decide your line length, as long as it has fewer than 99 characters.

It is beyond the scope of this document to summarise the PEP8 conventions, but here are some of the most salient points:

- Indentation of four spaces. **No tabs. Never.**
- Two blank lines between functions and classes. One blank line between methods in a class. A single line at the end of each file.
- Always use spaces around operators and assignments (`a = 1`). The only exception if for function and method keyword arguments (`my_function(1, key='a')`).
- No trailing spaces. You can configure your editor to strip the lines automatically for you.
- Imports go on the top of the file. Do **not** import more than one package in the same line (`import os, sys`). Maintain the namespace, do **not** import all functions in a package (`from os import *`). You can import multiple functions from the same package at the same time (`from os.path import dirname, basename`).
- Use single quotes for strings. Double quotes must be reserved for docstrings and string blocks.
- For inline comments, at least two spaces between the statement and the beginning of the comment (`a = 1  # This is a comment about a`).
- Class names must be in camelcase (`class MyClass`). Function, method, and variable names should be all lowercase separated by underscores for legibility (`def a_function_that_does_something`, `my_variable = 1`). For the latter ones, PEP8 allows some flexibility. The general rule of thumb is to make your function, method, and variable names descriptive and readable (void multiple words in all lowercase). As such, if you prefer to use camelcase (`aFunctionThatDoesSomething`, `myVariable = 1`) for your project that is accepted. When modifying somebody else's code, stick to their naming decisions.
- Use `is` for comparisons with `None`, `True`, or `False`: `if foo is not None:`.

### Docstrings

Docstrings are special comments, wrapped between two sets of three double quotes (`"""`). Their purpose is dual: on one side they provide clear, well structure documentation for each class and function in your code. But they are also intended to be read by an automatic documentation generator (see the [Automatic documentation generation](#automatic-documentation-generation) section).
For docstrings, follow [PEP257](https://www.python.org/dev/peps/pep-0257/). In our template, [main.py](./python/python_template/main.py) contains some examples of functions and classes with docstrings; use those as an example. In general:

- **All** code should be commented. **All** functions, classes, and methods should have a docstring.
- Use double quotes for docstrings; reserve single quotes for normal strings.
- Limit your docstrings lines to the same line length your are using for your code. **TODO: actually PEP237 recommends to use 72 characters. Do we follow that?**
- A complete docstring should start with a single line describing the general purpose of the function or class. Then a blank line and and in-depth description of the function or class in one or more paragraphs. A list of the input parameters (arguments and keywords) follows, and a description of the values returned, if any. If the class or function merits it, you should include an example of use.
- The docstring for the `__init__()` method in a class goes just after the declaration of the class and it explains the general use for the class, in addition to the list of parameters accepted by `__init__()`.
- Private methods and functions (those that start with an underscore) may not have a docstring **only** if their purpose is really obvious.
- In general, we prefer [Numpy style](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy) docstrings over [Google style](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html#example-google) docstrings, but you are free to choose one as long as you stick with it across all the product. Avoid style such as `param path: The path of the file to wrap` which are difficult to read.

### Linters

Do use a linter. These are plugins available for almost every editor (vim, emacs, Sublime Text, Atom) that are executed every time you save code and show you syntax error and where you are not following PEP8 conventions. They normally rely on an underlying library, usually [pylint](https://www.pylint.org/) or [flake8](http://flake8.pycqa.org/en/latest/). This template includes customised configuration files for both libraries. You can also place `.flake8` and `.pylintrc` files in your home directory and they will be used for all your projects (configuration files *in* the root of the project override the general configuration for that project).

While `pylint` is a more fully fleshed library, and provides estimates on code complexity, docstring linting, etc., it may be a bit excessive and verbose for most users. `flake8` provides more limited features, but its default configuration is usually what you want (and we enforce in SDSS). It is up to you to test them and decide which one to use.

### General advice

- Blank lines take only one byte; there is no reason for you not to use them frequently in your code and improve its legibility.
- Remember the [Zen of Python](https://www.python.org/dev/peps/pep-0020/). Explicit is better than implicit. Simple is better than complex.

## Testing

## Automatic documentation generation

### Sphinx

### Readthedocs

## TODO / Questions

- Licensing: should SDSS adopt a default license?
- Should we keep the python directory?
- Testing
    - pytest
    - Travis
    - Tox
    - Coverall
- Sphinx
    - Readthedocs
- Bibliography / tutorials.
- File headers: should we agree on a template?
- Travis configuration file.
- Zenodo
- test directory at the top level?
