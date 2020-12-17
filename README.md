# cookiecutter-python

This is a [cookiecutter](https://github.com/audreyr/cookiecutter) template for creating Python packages that adhere to the [SDSS standards](./STYLE.rst).

The full documentation on how to use this template can be found [here](http://sdss-python-template.readthedocs.io/en/latest/).

> **WARNING:** version 2 of the Python Template is significantly different from version 1, whose documentation can be found [here](http://sdss-python-template.readthedocs.io/en/latest/v1/v1.html).

## User Installation

To install and initialize this template:

```console
pip install invoke
pip install cookiecutter
cookiecutter https://github.com/sdss/python_template.git
```

If you want to install [version 1](https://github.com/sdss/python_template/tree/python-template-v1) of the template, you can do:

```console
cookiecutter https://github.com/sdss/python_template.git --checkout python-template-v1
```

During the installation, you will be asked a series of prompts to specify options and variable names, e.g. your name, the desired package name, etc. These definitions will be inserted into the package in designated places. The final prompts ask

* Do you want to use [setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html) or [poetry](https://python-poetry.org/) to manage your dependencies?
* What Sphinx theme do you want to use?
* Do you want to create a git repository out of your new package?
* Do you want to connect your new git repo to an account on github?

## What you get in this template

* Python 3 compatibility (Python 2 has been dropped as of verson 2 of the template).
* Pip-ready product.
* Sphinx Documentation with Read The Docs integration.
* Pytest testing framework.
* Improved logging, versioning, and configuration tools using [sdsstools](https://github.com/sdss/sdsstools), as well as commonly used tasks for building the documentation and deploying to PyPI.
* Continuous Integration with Travis.
* Code coverage with [codecov](https://codecov.io).
* Module file.

## Coding standards

Before you start writing your code, make sure to read and understand the [SDSS coding standards](./STYLE.rst).

## Developers

If you are developing on this template, first clone the product:

```console
git clone https://github.com/sdss/python_template.git
```

Now edit / add to the code as one normally does. This package contains a Jinja2 template structure, with variable substitution that occurs upon installation. Variables to be inserted into the template are defined in `cookiecutter.json`. To reference a variable inside the template structure use the Jinja2 double bracket nomenclature.

```console
{{cookiecutter.full_name}}
```

To test install the cookiecutter package locally, run:

```console
cookiecutter [path_to_my_local_clone_directory]
```

It is good practice to test install the package locally before you commit any changes to ensure the package can properly install without error.

You can also fork this template or create new branches with your specific preferences; then just install it by doing

```console
cookiecutter https://github.com/sdss/python_template.git --checkout <branch>
```
