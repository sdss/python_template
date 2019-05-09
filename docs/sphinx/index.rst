.. title:: Welcome to SDSS Python Template documentation!

Welcome to SDSS Python Template documentation!
==============================================

This page describes the `SDSS Python Template <https://github.com/sdss/python_template>`_ as well as the :doc:`coding standards <standards>`.

See :doc:`what's new <changelog>`.

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
* :ref:`Configuration file <conf-log-section>` and improved :ref:`logging <conf-log-section>`.
* the SDSS :ref:`tree and sdss_access <sdsspy>` python packages.

Directory Contents
------------------

* **cextern**: The directory for placing C code to be compiled
* **docs**: The directory for Sphinx documentation and other docu-related files
* **etc**: The directory containing your SDSS modulefile and other etc
* **python**: Your new python package directory
* **python/package_name/core**: A directory for high-level core classes used in your product.  Contains a set of custom python Exceptions.
* **python/package_name/etc**: An etc directory with text files that will be installed with the product. Contains a YAML configuration file that is ready by the package when imported.
* **python/package_name/utils**: General-use tools, including a custom logger and colour printing routines.
* **python/package_name/tests**: The directory containing the tests for the package. Includes a ``conftest.py`` file with basic configuration using `pytest <https://docs.pytest.org/en/latest/>`_.
* **CHANGELOG.rst**: A file documenting changes to your code, e.g. new features, fixed issues, or bug-fixes.
* **CODEOWNERS**: A file assigning ownership of the code to the package or components of the package to various users
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

To install and initialize a new product from the template run ::

    pip install invoke
    pip install bumpversion
    pip install cookiecutter
    cookiecutter https://github.com/sdss/python_template.git

During the installation `cookiecutter <https://github.com/audreyr/cookiecutter>`__ will ask you a series of prompts to specify options and variable names, e.g. your name, the repository/folder name, the package name (which can be identical to the repository name), etc. These definitions will be inserted into the package in designated places to customise it for you.

The **create_git_repo** prompt asks ``do you want to create a git repository out of your new package?``.  If you answer ``yes``, the product will be initialised as a git repository.  The final prompts ask ``did you already create a new repository on Github?`` and ``what is your Github username?``.  If you answer ``yes``, and specify a name, a remote origin will be added to your new git repository and will be pushed to Github.  If not, `create a blank GitHub repository <https://help.github.com/articles/creating-a-new-repository/>`_ (either at the `SDSS organisation <https://github.com/sdss>`_ or in your personal account) and copy the URL provided by GitHub.  Make sure the Github repository is initially empty. In the root of your local product run ::

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

It is recommended to always do a dry run of your bump before the real thing to make sure it will go smoothly.  You can do it with::

    bumpversion patch --dry-run --verbose

The default configuration of bumpversion is to always perform a commit whenever you bump to the next version.  You can specify to also create a new tag of your version with::

    bumpversion patch --tag

This will create a new tag locally with the new bumped version as the tag name.  You can push the tag to Github with::

    git push origin [tagname]

If you release and tag a new version, don't forget to do ``bumpversion patch`` to increment to the next `dev` version.


.. _tests-section:

Writing and running tests
-------------------------

The ``tests`` directory contains some examples on how to write and run tests for your package using `pytest`_. Use the `conftest.py <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/python/%7B%7Bcookiecutter.package_name%7D%7D/tests/conftest.py>`_ file to define `fixtures <https://docs.pytest.org/en/latest/fixture.html>`__ and other `pytest`_-specific features. cd'ing to the ``tests`` directory and typing ``pytest`` will recursively run all the tests in files whose filename starts with ``test_``.

If you prefer to use `unittest <https://docs.python.org/3/library/unittest.html>`_ or `nose <https://nose2.readthedocs.io/en/latest/getting_started.html>`_ feel free to remove those files.


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

The cookiecut product documentation is ready to be built and integrated with Read The Docs. As with Travis and Coveralls above, you will need to commit the products to a GitHub repository first. SDSS has a `Read The Docs <http://readthedocs.io/>`_ account that is the preferred place to integrate the documentation. You can request access to the account by emailing ``admin[at]sdss[dot]org``. Alternatively, you can deploy your product in your own Read the Docs account and add the user ``sdss`` as a maintainer from the admin menu.

Probably you will receive a message saying that the integration of the product is not complete and that you need to set up a webhook. To do that, got to the admin setting of the new Read The Docs project. In ``Intergations`` add a new integration and copy the link to the webhook. Then go to the GitHub repository settings and in the ``Webhooks`` section add a new webhook with the URL you just copied. Once you submit, any push to the master branch of the GitHub repo should produce a new built of the documentation. You can find more details on the webhook set up `here <https://docs.readthedocs.io/en/latest/webhooks.html>`_.

The product configuration for Read The Docs can be found in `readthedocs.yml <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/readthedocs.yml>`_. By default, the Sphinx documentation will be built using Python 3.6 and using the requirements specified in `requirements_doc.txt <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/requirements_doc.txt>`_. You can change those settings easily.


.. _conf-log-section:

Configuration file and logging
------------------------------

Your new product contains a `YAML <http://yaml.org/>`_ configuration file in the ``python/[product_name]/etc/`` directory. YAML is significantly superior to other alternatives such as `configparser <https://docs.python.org/3/library/configparser.html>`__; it provides typed values, a clear data structure, and powerful parsing libraries. When you import the package, the configuration can be accessed as a dictionary using the ``config`` attribute. For example ::

    import mypython
    print(mypython.config['option1']['suboption1'])
    >>> 2.0
    print(mypython.config['option1']['suboption2'])
    >>> 'some text'

If the user creates a custom configuration file in ``~/.config/mypython/mypython.yml``, the contents of that file will be used to update the default options. For instance, if you create a file with the contents

.. code-block:: yaml

    option1:
        suboption2: "a different text"

the code above would return ::

    print(mypython.config['option1']['suboption1'])
    >>> 2.0
    print(mypython.config['option1']['suboption2'])
    >>> 'a different text'

Another possibility is to define an environment variable ``$MYPYTHON_CONFIG_PATH`` pointing to the user configuration file to use. If the environment variable is set, it overrides the default location for the user configuration file.

The package also includes a logging object built around Python's `logging <https://docs.python.org/3/library/logging.html>`__ module. Our custom logger allows to file and screen at the same time and provides more colourful tracebacks and warnings. From anywhere in your code you can do ::

    from mypython import log
    log.info('Some information that we want to log')
    >>> [INFO]: Some information that we want to log

Available levels are ``.debug``, ``.info``, ``.error``, and ``.critical``. For warnings, use `warnings <https://docs.python.org/3/library/warnings.html>`__ module.

By default, the file logger is not enabled. To start logging to file do ::

    log.start_file_logger('~/.mypython/mypython.log')

where ``'~/.mypython/mypython.log'`` is the path of the file to which we want to log. If the file exists, the previous file is backed up by adding a timestamp to the extension. File logs are automatically backed up at midnight (see `TimedRotatingFileHandler <https://docs.python.org/2/library/logging.handlers.html>`__).

On initialisation, the screen logger will only show messages with level ``INFO`` or above. The file logger default level is ``DEBUG``. Levels can be changed in runtime ::

    # Sets the screen minimum level to DEBUG
    import logging
    log.sh.setLevel(logging.DEBUG)

    # Sets the file level to CRITICAL
    log.fh.setLevel(logging.CRITICAL)

The current log can be saved as ::

    log.save_log('~/Downloads/copy_of_log.log')


.. _deploying-section:

Deploying your product
----------------------

This section explains how to deploy a new version of your product to `PyPI <https://pypi.python.org/pypi>`_ so that it becomes `pip <https://pip.pypa.io/en/stable/>`_-installable. All SDSS products should be deployed to the SDSS dedicated PyPI account, access to which can be requested to ``admin[at]sdss[dot]org``. First you will need to create a ``~/.pypirc`` file with the following content ::

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

The `NAME` argument inside your `setup.py` specifies the name of the package as it appears in `PyPi` and how it will be installed.  To avoid potential conflicts with existing packages, all SDSS package pip-names should adhere to the format ``sdss-[pkgname]``.  E.g. the Python package
`tree` would be called `sdss-tree`.  The python package `sdss_access` would be called `sdss-access`.


How to modify this template
---------------------------

This template is built using `Cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_.  To add content to or expand this template, you must first check out the main template product using git::

    git clone https://github.com/sdss/python_template

Now you have the development version of this template.  The two main components need are a `cookiecutter.json` file and a `{{cookiecutter.repo_name}}` directory.  Cookiecutter templates use the `Jinja2 <http://jinja.pocoo.org/docs/2.10/>`_ templating language to define variable substitution, using double bracket notation, e.g. `{{variable_name}}`.  All customizable content to be inserted by the user is defined using this notation.

* **{{cookiecutter.repo_name}}**: the top-level directory defining the installed python package.  Everything below this directory belongs to the Python package that gets installed by the user.
* **cookiecutter.json**: A JSON file containing a dictionary of key:value pairs of variables defined in the template, with their default values.  These keys are referenced throughout the template with `{{cookiecutter.key}}`.

Upon installation of the template by a user, the variables defined in the `cookiecutter.json` file, or by the user during install, get substituted into their respective reference places.

Please, *do not* modify the master branch directly unless otherwise instructed. Instead, develop your changes in a branch or fork and, when ready to merge, create a pull request.

.. _sdsspy:

SDSS tree and sdss_access
-------------------------

This template includes the SDSS `tree <http://github.com/sdss/tree>`_ and `sdss_access <http://github.com/sdss/sdss_acess>`_ Python packages.  This template adds these products as required dependencies in your installed project's `requirements.txt` file.  We encourage you to use these packages inside your code.  The `tree` package is designed to set up the SDSS SAS environment system dynamically within your Python environment.  The `sdss_access` package is designed to provide local and remote filesystem path generation and downloading.  To use these yourself, you may need to install them::

    pip install sdss-tree
    pip install sdss-access

See the `tree <http://sdss-tree.readthedocs.io/en/latest/>`_ and `sdss_access <http://sdss-access.readthedocs.io/en/latest/>`_ `readthedocs` for full documentation on each package, but in brief, to use the `tree`::

    # loads the full SAS using the sdsswork configuration.  You only need to do this one per Python session.
    from tree import Tree
    my_tree = Tree()

and to use `sdss_access`::

    # generate a local path to a file
    from sdss_access.path import Path
    path = Path()
    filepath = path.full('mangacube', drpver='v2_3_1', plate='8485', '1901')
