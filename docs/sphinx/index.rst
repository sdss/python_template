.. title:: Welcome to SDSS Python Template documentation!

Welcome to SDSS Python Template documentation!
==============================================

This page describes the `SDSS Python Template <https://github.com/sdss/python_template>`_ as well as the :doc:`coding standards <standards>`.

User Installation
-----------------

To install and initialize the template:

.. code-block:: bash

    pip install invoke
    pip install cookiecutter
    cookiecutter https://github.com/sdss/python_template.git

or to optionally install a specific branch:

.. code-block:: bash

    cookiecutter https://github.com/sdss/python_template.git --checkout [branchname]

During the installation, you will be asked a series of prompts to specify options and variable names, e.g. your name, the desired package name, etc. These definitions will be inserted into the package in designated places.  The final prompts ask ::

    * do you want to install the new python package with python setup.py install?
    * do you want to create a git repository out of your new package?
    * do you want to connect your new git repo to an account on github?


Using the template
------------------

Once cookiecut, the resulting directory is a totally functional, if very simple, Python package. It can be installed by running ``python setup.py install``. Alternatively, you can add the path to the template ``python`` directory to your ``$PYTHONPATH`` environment variable.

If during the setup you told cookiecutter to connect the new product to GitHub, your git remote should already be set. You can confirm it by doing ``git remote -a``. You still need to create the GitHub repository. To do so, got to https://github.com/sdss/ (or any other organisation where you want to upload your code) and create a new repository with the name of the new product.

If you did not setup GitHub during the cookiecutter installation, no worries. Create the GitHub repository, copy the remote URL and then, run ::

    git remote add origin https://github.com/sdss/your_product

in your local product.


Bumping a version
-----------------

The python template you cookiecut uses `bumpversion <https://github.com/peritus/bumpversion>`_ to increase the version of your product. The bumpversion configuration is defined in the `.bumpversion.cfg <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/.bumpversion.cfg>`_ file in your new product. You should read the bumpversion documentation for details, but usually your workflow will be as follows: once you are ready to start working on a new version do ::

    bumpversion bugfix

This will increase your version from ``X.Y.Z`` to ``X.Y.(Z+1)dev0`` (e.g., ``1.2.3`` to ``1.2.4dev0``) everywhere in your product and commit the changes. You can alternatively do ``bumpversion minor`` or ``bumpversion major`` to change the minor or major version. Once you are ready to release the version, do ::

    bumpversion release

to remove the ``dev`` suffix. You can also do ``bumpversion bugfix release`` to release a new bugfix version without passign through the ``dev`` step.

.. Indices and tables
.. ==================
..
.. * :ref:`genindex`
.. .. * :ref:`modindex`
.. * :ref:`search`
