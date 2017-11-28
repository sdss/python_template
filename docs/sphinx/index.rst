.. title:: Welcome to SDSS Python Template documentation!

Welcome to SDSS Python Template documentation!
==============================================

This page describes the `SDSS Python Template <https://github.com/sdss/python_template>`_ as well as the :doc:`coding standards <standards>`.

Screencast
----------

**[A screencast showing how to use the cookiecut product]**

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

    bumpversion patch

This will increase your version from ``X.Y.Z`` to ``X.Y.(Z+1)dev`` (e.g., ``1.2.3`` to ``1.2.4dev``) everywhere in your product and commit the changes. You can alternatively do ``bumpversion minor`` or ``bumpversion major`` to change the minor or major version. Once you are ready to release the version, do ::

    bumpversion release

to remove the ``dev`` suffix. You can also do ``bumpversion patch release`` to release a new patch version without passing through the ``dev`` step.


Connecting your product to Travis
---------------------------------

The template includes a basic setup for `Travis CI <https://travis-ci.org/>`_ and `Coveralls <https://coveralls.io/>`_. The configuration is defined in the `.travis.yml <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/.travis.yml>`_ and `.coveragerc <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/.coveragerc>`_ files.

Once you have created the GitHub repository for the product, you can go to your `Travis CI <https://travis-ci.org>`_ account and click on ``Add a new repository``. Then search for the new product and flip the switch to initiate the integration. You can do the same thing for `Coveralls <https://coveralls.io/>`_. Each new push to the repository will trigger a Travis run that, if successful, will update the coverage report.

**[Is this correct? Add more details]**


Connecting your product to Read The Docs
----------------------------------------

The cookiecut product documentation is ready to be built and integrated with Read The Docs. As with Travis and Coveralls above, you will need to commit the products to a GitHub repository first. SDSS has a `Read The Docs <http://readthedocs.io/>`_ account that is the preferred place to integrate the documentation. If you have access to the account, just go there and add the repository. Probably you will receive a message saying that the integration of the product is not complete and that you need to set up a webhook. To do that, got to the admin setting of the new Read The Docs project. In ``Intergations`` add a new integration and copy the link to the webhook. Then go to the GitHub repository settings and in the ``Webhooks`` section add a new webhook with the URL you just copied. Once you submit, any push to the master branch of the GitHub repo should produce a new built of the documentation. You can find more details on the webhook set up `here <https://docs.readthedocs.io/en/latest/webhooks.html>`_.

The product configuration for Read The Docs can be found in `readthedocs.yml <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/readthedocs.yml>`_. By default, the Sphinx documentation will be built using Python 3.5 and using the requirements specified in `requirements_doc.txt <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/requirements_doc.txt>`_. You can change those settings easily.


Using invoke
------------

The product includes several macros to automate frequent tasks using `invoke <http://www.pyinvoke.org/>`_. To get a list of all the available tasks, from the root of your cookiecut project, do ::

    invoke -l

The documentation can be compiled by doing ``invoke docs.build`` and then shown in your browser with ``invoke docs.show``. Another useful macro, ``invoke deploy``, automates the process of deploying a new version by creating new distribution packages and uploading them to PyPI (see deploying_).

You can add new tasks to the `tasks.py <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/tasks.py>`_ file.


.. _deploying:

Deploying your product
----------------------
