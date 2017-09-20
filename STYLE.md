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

Some resources that can be useful to write code that is Python 2 and 3-compatible, and to port code from 2 to 3.

- TODO: link to a web with advice to write code for 2 and 3.
- TODO: description and link to `six.py`.
- TODO: description and link to `2to3`.


## Coding style

SDSS code follows the [PEP8 standard](https://www.python.org/dev/peps/pep-0008/). Please, read that document carefully and follow at every, unless there are very good reasons not to.

The only point in which SDSS slightly diverges from PEP8 is the line length. While the suggested PEP8 maximum line length of 79 characters is recommended, lines up to 99 characters are accepted. When deciding what line length to use follow this rule: if you are modifying code that is not nominally owned by you, respect the line length employed by the owner of the product; if you are creating a new product that you will own, feel free to decide your line length, as long as it has fewer than 99 characters.

It is beyond the scope of this document to summarise the PEP8 conventions, but here are some of the most salient points:

- Indentation of four spaces. **No tabs. Never.***
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


## Automatic documentation generation

### Sphinx

### Readthedocs


## TODO:

- PEP8 and docstrings
- Deployment
- Testing
    - pytest
    - Travis
    - Tox
    - Coverall
- Sphinx
    - Readthedocs
- Bumpversion
- General documentation / tutorials.
