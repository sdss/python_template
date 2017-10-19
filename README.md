# cookiecutter-python

This is a [cookiecutter](https://github.com/audreyr/cookiecutter) template for creating Python packages that adhere to the [SDSS standard](./\{\{cookiecutter.package\}\}/STYLE.md).

## Installation

To install and initialize this template:

    pip install invoke
    pip install cookiecutter
    cookiecutter https://github.com/sdss/python_template.git

or to optionally install a specific branch:

    cookiecutter https://github.com/sdss/python_template.git --checkout [branchname]


## Developers

If you are developing on this template, first clone the product:

    git clone https://github.com/sdss/python_template.git

Now edit as one normally does.  To test the cookiecutter package locally, run:

    cookiecutter [path_to_my_local_clone_directory]


## What you get in this template

* Python 2/3 compatibility
* Pip-ready product
* Sphinx Documentation with ReadtheDocs hook
* Pytest Testing Framework
* Tox for Multiple Python Environment Testing
* Improved Logging
* Versioning with BumpVersion
* Continuous Integration with Travis
* Code Coverage with Coveralls
* Module File
* Invoke for shell tasks

## Coding standards

Before you start writing your code, make sure to read and digest the [SDSS coding standards](./\{\{cookiecutter.package\}\}/STYLE.md).

## TODO / Questions

- Licensing: should SDSS adopt a default license?
- Should we keep the python directory?
- Tox
- Bibliography / tutorials.
- Travis configuration file.
- Zenodo
- test directory at the top level?
- reStructured vs markdown. Should we adopt rst for readmes and style?
- CLI: argparse vs click vs invoke?
- Use inline docstring for attributes or section in header docstring?
