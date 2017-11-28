# cookiecutter-python

This is a [cookiecutter](https://github.com/audreyr/cookiecutter) template for creating Python packages that adhere to the [SDSS standard](./\{\{cookiecutter.repo_name\}\}/STYLE.rst).

## User Installation

To install and initialize this template:

    pip install invoke
    pip install cookiecutter
    cookiecutter https://github.com/sdss/python_template.git

or to optionally install a specific branch:

    cookiecutter https://github.com/sdss/python_template.git --checkout [branchname]

During the installation, you will be asked a series of prompts to specify options and variable names, e.g. your name, the desired package name, etc. These definitions will be inserted into the package in designated places.  The final prompts ask

* do you want to install the new python package with python setup.py install?
* do you want to create a git repository out of your new package?
* do you want to connect your new git repo to an account on github?


## Developers

If you are developing on this template, first clone the product:

    git clone https://github.com/sdss/python_template.git

Now edit / add to the code as one normally does.  This package contains a Jinja2 template structure, with variable substitution that occurs upon installation. Variables to be inserted into the template are defined in `cookiecutter.json`.  To reference a variable inside the template structure use the Jinja2 double bracket nomenclature.

   {{cookiecutter.full_name}}

To test install the cookiecutter package locally, run:

    cookiecutter [path_to_my_local_clone_directory]

It is good practice to test install the package locally before you commit any changes to ensure the package can properly install without error.

## What you get in this template

* Python 2/3 compatibility
* Pip-ready product
* Sphinx Documentation with Read The Docs integration
* Pytest Testing Framework
* Tox for Multiple Python Environment Testing (in a future versions)
* Improved Logging
* [Versioning with BumpVersion](https://github.com/peritus/bumpversion)
* Continuous Integration with Travis
* Code Coverage with Coveralls
* Module File
* Invoke for shell tasks

## Coding standards

Before you start writing your code, make sure to read and digest the [SDSS coding standards](./\{\{cookiecutter.repo_name\}\}/STYLE.rst).

## TODO / Questions

- Should we keep the python directory? Note: we agreed on keeping the python directory for the template but not make it a SDSS requirement.
- Tox
- Bibliography / tutorials.
- Travis configuration file.
- Zenodo. Note: Brian will write a section for the style guide.
- test directory at the top level? Note: same as for the python directory.
- reStructured vs markdown. Should we adopt rst for readmes and style?
- CLI: argparse vs click vs invoke?
- Use inline docstring for attributes or section in header docstring?
