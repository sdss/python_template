.. title:: Welcome to SDSS Python Template documentation!

Welcome to SDSS Python Template documentation!
==============================================

This page describes the `SDSS Python Template <https://github.com/sdss/python_template>`_ as well as the :doc:`coding standards <standards>`.


What you get with this template
-------------------------------

* Python 2/3 compatibility
* `Pytest <https://docs.pytest.org/en/latest/>`_ testing framework
* Continuous Integration with :ref:`Travis <travis-section>` and `Coveralls <https://coveralls.io/>`_
* :ref:`Pip <deploying-section>`-ready product
* :ref:`Sphinx Documentation <sphinx-section>` with :ref:`Read The Docs <rtd-section>` integration
* Versioning with :ref:`BumpVersion <bumpversion-section>`.
* :ref:`Invoke <invoke-section>` for shell tasks
* SDSS-compliant `license file <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/LICENSE.md>`_.
* `Module file <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/etc/%7B%7Bcookiecutter.package_name%7D%7D.module>`_.
* Package configuration file


Directory Contents
------------------

* **cextern**: The directory for placing C code to be compiled
* **docs**: The directory for Sphinx documentation and other docu-related files
* **etc**: The directory containing your SDSS modulefile and other etc
* **python**: Your new python package directory
* **CHANGELOG.rst**: A file documenting changes to your code, e.g. new features, fixed issues, or bug-fixes.
* **README.rst**: A file describing your package.  This will be the main display on Github.
* **STYLE.rst**: The SDSS style guide for best coding practices.
* **LICENSE.md**: The open source license for your product.  DO NOT DELETE.
* **setup.py**: The setup for your pip-deployable product.  Also used when installing manually with `python setup.py install`.
* **tasks.py**: A list of all invoke tasks available.
* **requirements[_xxx].txt**: These files list all Python packages that are dependencies for your product.  Needed by pip.
* **readthedocs.yml**: The configuration file for Read The Docs.
* **.travis.yml**:  The configuration file for Travis CI.
* **.bumpversion.cfg**: The configuration file for Bumpversion.
* **.coveragerc**: The configuration file for python code coverage and Coveralls.


Creating a new product
----------------------

To install and initialize a new product from the template run

.. code-block:: bash

    pip install invoke
    pip install cookiecutter
    cookiecutter https://github.com/sdss/python_template.git

During the installation you will be asked a series of prompts to specify options and variable names, e.g. your name, the repository/folder name, the package name (which can be identical to the repository name), etc. These definitions will be inserted into the package in designated places.

The **create_git_repo** prompt asks ``do you want to create a git repository out of your new package?``.  If you answer ``yes``, the product will be initialised as a git repository.  The final prompts ask ``did you already create a new repository on Github?`` and ``what is your Github username?``.  If you answer ``yes``, and specify a name, a remote origin will be added to your new git repository and will be pushed to Github.  If not, `create a GitHub repository <https://help.github.com/articles/creating-a-new-repository/>`_ (either at the `SDSS organisation <https://github.com/sdss>`_ or in your personal account) and copy the URL provided by GitHub. In the root of your local product run ::

    git remote add origin GITHUB_URL
    git push

The new product can be installed in your system by running ``python setup.py install``. For development, however, it is usually better to add the product path to your ``PYTHONPATH``. In bash add the following line to your ``~/.bashrc`` (modify accordingly for csh or other shells) ::

    export PYTHONPATH=/path/to/your/product/python:$PYTHONPATH

Now you have a totally functional, if very simple, Python package connected to a GitHub repository. The following sections explain how to use the features included in the template and how to connect it with different online services. Before you continue, this may be a good time to read the :doc:`SDSS coding standards <standards>` and make sure your code complies with them.


.. _bumpversion-section:

Bumping a version
-----------------

The python template you cookiecut uses `bumpversion <https://github.com/peritus/bumpversion>`_ to increase the version of your product. First, you need to install ``bumpversion`` by doing ::

    pip install bumpversion

The bumpversion configuration is defined in the `.bumpversion.cfg <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/.bumpversion.cfg>`_ file in your new product. You should read the bumpversion documentation for details, but usually your workflow will be as follows: once you are ready to start working on a new version do ::

    bumpversion patch

This will increase your version from ``X.Y.Z`` to ``X.Y.(Z+1)dev`` (e.g., ``1.2.3`` to ``1.2.4dev``) everywhere in your product and commit the changes. You can alternatively do ``bumpversion minor`` or ``bumpversion major`` to change the minor or major version. Once you are ready to release the version, do ::

    bumpversion release

to remove the ``dev`` suffix. You can also do ``bumpversion patch release`` to release a new patch version without passing through the ``dev`` step.

The default configuration of bumpversion is to always perform a commit whenever you bump to the next version.  You can specify to also create a new tag of your version with::

    bumpversion patch --tag

This will create a new tag locally with the new bumped version as the tag name.  You can push the tag to Github with::

    git push origin [tagname]

If you release and tag a new version, don't forget to do ``bumpversion patch`` to increment to the next `dev` version.


.. _travis-section:

Connecting your product to Travis
---------------------------------

The template includes a basic setup for `Travis CI <https://travis-ci.org/>`__ and `Coveralls <https://coveralls.io/>`_. The configuration is defined in the `.travis.yml <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/.travis.yml>`_ and `.coveragerc <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/.coveragerc>`_ files.

Once you have created the GitHub repository for the product, you can go to your `Travis CI <https://travis-ci.org>`__ account (create one if you don't have it) and click on ``Add a new repository``. Then search for the new product and flip the switch to initiate the integration. You can do the same for `Coveralls <https://coveralls.io/>`_. Each new push to the repository will trigger a Travis run that, if successful, will update the coverage report.


.. _invoke-section:

Using invoke
------------

The product includes several macros to automate frequent tasks using `Invoke <http://www.pyinvoke.org/>`_. To get a list of all the available tasks, from the root of your cookiecut project, do ::

    invoke -l

The documentation can be compiled by doing ``invoke docs.build`` and then shown in your browser with ``invoke docs.show``. Another useful macro, ``invoke deploy``, automates the process of deploying a new version by creating new distribution packages and uploading them to PyPI (see deploying-section_).

You can add new tasks to the `tasks.py <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/tasks.py>`__ file.


.. _sphinx-section:

How to build Sphinx Documentation
---------------------------------

This template includes `Sphinx <http://www.sphinx-doc.org/en/stable/>`_ documentation, written using the `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ format.  The documentation is located inside your python package, in a `docs/sphinx/` directory.  You can build the existing Sphinx documentation with::

Using invoke::

    invoke docs.build

Alternatively, navigate to your python package's `docs/sphinx/` directory and type::

    make html

This will build your documentation, converting the rst files into html files.  The output html files live in the `docs/sphinx/_build` subdirectory.  To both build and display the documentation, type::

    # builds and displays
    invoke docs.show

The main page of your documentation lives at `docs/sphinx/_build/html/index.html`.  New documentation must be written in the rst syntax for Sphinx to understand and properly build html files.

The template includes an example on how to automatically document the docstrings in your code. In `docs/sphinx/api.rst` you'll see the lines ::

    .. automodule:: mypython.main
       :members:
       :undoc-members:
       :show-inheritance:

You can add similar blocks of code for other modules. See the Sphinx `autodoc <http://www.sphinx-doc.org/en/stable/ext/autodoc.html>`_ for more details. The :ref:`coding standards <style-docstring>` include a section on how to write good docstrings to document your code.


.. _rtd-section:

Connecting your product to Read The Docs
----------------------------------------

The cookiecut product documentation is ready to be built and integrated with Read The Docs. As with Travis and Coveralls above, you will need to commit the products to a GitHub repository first. SDSS has a `Read The Docs <http://readthedocs.io/>`_ account that is the preferred place to integrate the documentation. If you have access to the account, just go there and add the repository. Probably you will receive a message saying that the integration of the product is not complete and that you need to set up a webhook. To do that, got to the admin setting of the new Read The Docs project. In ``Intergations`` add a new integration and copy the link to the webhook. Then go to the GitHub repository settings and in the ``Webhooks`` section add a new webhook with the URL you just copied. Once you submit, any push to the master branch of the GitHub repo should produce a new built of the documentation. You can find more details on the webhook set up `here <https://docs.readthedocs.io/en/latest/webhooks.html>`_.

The product configuration for Read The Docs can be found in `readthedocs.yml <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/readthedocs.yml>`_. By default, the Sphinx documentation will be built using Python 3.5 and using the requirements specified in `requirements_doc.txt <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/requirements_doc.txt>`_. You can change those settings easily.


.. _deploying-section:

Deploying your product
----------------------

This section explains how to deploy a new version of your product to `PyPI <https://pypi.python.org/pypi>`_ so that it becomes `pip <https://pip.pypa.io/en/stable/>`_-installable. All SDSS products should be deployed to the SDSS dedicated PyPI account, access to which can be requested to **XXX@sdss.org**. First you will need to create a ``~/.pypirc`` file with the following content ::

    [distutils]
    index-servers=
    pypi

    [pypi]
    repository = https://pypi.python.org/pypi
    username = sdss
    password = [request this password]

To deploy a new release you will need `twine <https://pypi.python.org/pypi/twine>`_. To install it ::

    pip install twine

Then, from the root of your product, run ::

    invoke deploy

which will create source and `wheel <https://pythonwheels.com/>`_ distributions of your package and upload them to PyPI. The command above is equivalent to running ::

    python setup.py sdist bdist_wheel --universal
    twine upload dist/*


How to modify this template
---------------------------

This template is built using `Cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_.  To add content to or expand this template, you must first check out the main template product using git::

    git clone https://github.com/sdss/python_template

Now you have the development version of this template.  The two main components need are a `cookiecutter.json` file and a `{{cookiecutter.repo_name}}` directory.  Cookiecutter templates use the `Jinja2 <http://jinja.pocoo.org/docs/2.10/>`_ templating language to define variable substitution, using double bracket notation, e.g. `{{variable_name}}`.  All customizable content to be inserted by the user is defined using this notation.

* **{{cookiecutter.repo_name}}**: the top-level directory defining the installed python package.  Everything below this directory belongs to the Python package that gets installed by the user.
* **cookiecutter.json**: A JSON file containing a dictionary of key:value pairs of variables defined in the template, with their default values.  These keys are referenced throughout the template with `{{cookiecutter.key}}`.

Upon installation of the template by a user, the variables defined in the `cookiecutter.json` file, or by the user during install, get substituted into their respective reference places.

Please, *do not* modify the master branch directly, unless otherwise instructed. Instead, develop your changes in a branch and, when ready to merge, create a pull request.
