.. title:: SDSS Python Template documentation

SDSS Python Template
====================

.. note::
    This is the documentation for Python Template 2. The documentation for version 1 can be found :doc:`here <v1/v1>`.

This page describes the `SDSS Python Template <https://github.com/sdss/python_template>`_ as well as the :doc:`coding standards <../standards>`.

See :doc:`what's new <../changelog>`.


.. contents:: **Table of Contents**


What you get with this template
-------------------------------

* Python 3 compatibility (if you need Python 2/3 compatibility, check the :ref:`template version 1 <template-v1>`).
* `Pytest <https://docs.pytest.org/en/latest/>`_ testing framework.
* Continuous Integration with :ref:`Travis <travis-section-v2>` and `codecov <https://codecov.io>`_.
* :ref:`pip <deploying-section-v2>`-ready product.
* Dependency and metadata handling using :ref:`setuptools or poetry <packaging-section-v2>`.
* :ref:`Sphinx Documentation <sphinx-section-v2>` with :ref:`Read The Docs <rtd-section-v2>` integration.
* SDSS-compliant `license file <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.package_name%7D%7D/LICENSE.md>`_.
* `Module file <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.package_name%7D%7D/etc/%7B%7Bcookiecutter.package_name%7D%7D.module>`_.
* :ref:`Configuration file <conf-log-section-v2>` and improved :ref:`logging <conf-log-section-v2>`.
* Pre-defined scripts for frequently used :ref:`tasks <tasks-section-v2>`.
* The SDSS :ref:`tree and sdss_access <sdsspy-v2>` python packages.


Creating a new product
----------------------

To install and initialize a new product from the template run ::

    pip install invoke
    pip install cookiecutter
    cookiecutter https://github.com/sdss/python_template.git

During the installation `cookiecutter <https://github.com/audreyr/cookiecutter>`__ will ask you a series of prompts to specify options and variable names, e.g. your name, the repository/folder name, the package name (which can be identical to the repository name), etc. These definitions will be inserted into the package in designated places to customise it for you.

After asking for your name and emails, the cookiecutter process will prompt you for a **package_name** and a **pip_name**. The former is the name that you want to use when *importing* the product (``from package_name import main``) while the former is the name you want to use to publish your product to PyPI and make it pip-installable (``pip install pip_name``). While ``package_name`` and ``pip_name`` could be the same, normally we prefix the ``package_name`` with ``sdss-`` when publishing it. So, if your product is called ``mycamera``, its pip/PyPI name would be ``sdss-mycamera``. We talk about it in detail in :ref:`deploying-section-v2`.

The **create_git_repo** prompt asks ``do you want to create a git repository out of your new package?``.  If you answer ``yes``, the product will be initialised as a git repository.  The final prompts ask ``did you already create a new repository on Github?`` and ``what is your Github organisation?``.  If you answer ``yes``, and specify a name, a remote origin will be added to your new git repository and will be pushed to Github.  If not, `create a blank GitHub repository <https://help.github.com/articles/creating-a-new-repository/>`_ (either at the `SDSS organisation <https://github.com/sdss>`_ or in your personal account) and copy the URL provided by GitHub.  Make sure the Github repository is initially empty. In the root of your local product run ::

    git remote add origin GITHUB_URL
    git push

The new product can be installed in your system by running ``pip install .``. For development, however, it is usually better to add the product path to your ``PYTHONPATH`` or create a virtual environment. We talk about it in the :ref:`developing-section-v2` section. To modify your PYTHONPATH, in bash, add the following line to your ``~/.bashrc`` (modify accordingly for csh or other shells) ::

    export PYTHONPATH=/path/to/your/product/python:$PYTHONPATH

Now you have a totally functional, if very simple, Python package connected to a GitHub repository. The following sections explain how to use the features included in the template and how to connect it with different online services. Before you continue, this may be a good time to read the :doc:`SDSS coding standards <../standards>` and make sure your code complies with them.


Directory Contents
------------------

* **cextern**: The directory for placing C code to be compiled
* **docs**: The directory for Sphinx documentation and other docu-related files
* **etc**: The directory containing your SDSS modulefile and other etc
* **python**: Your new python package directory
* **python/package_name/exceptions**: A custom python Exceptions.
* **python/package_name/etc**: An etc directory with text files that will be installed with the product. Contains a YAML configuration file that is ready by the package when imported.
* **tests**: The directory containing the tests for the package. Includes a ``conftest.py`` file with basic configuration using `pytest <https://docs.pytest.org/en/latest/>`_.
* **CHANGELOG.rst**: A file documenting changes to your code, e.g. new features, fixed issues, or bug-fixes.
* **CODEOWNERS**: A file assigning ownership of the code to the package or components of the package to various users
* **README.md**: A file describing your package.  This will be the main display on Github.
* **LICENSE.md**: The open source license for your product.  DO NOT DELETE.
* **readthedocs.yml**: The configuration file for Read The Docs.
* **.travis.yml**:  The configuration file for Travis CI.

Depending or whether you choose to use setuptools or poetry, you will also get the relevant ``setup.cfg``, ``setup.py``, and ``pyproject.toml``.


.. _packaging-section-v2:

Packaging and dependency management
-----------------------------------

During the cutting process you'll be asked what packaging system, setuptools or poetry, you want to use. This is an important decision that will change the files provided with the template and how you manage your dependencies and packaging. While it's possible to switch between systems after cutting the product, it's not totally trivial so it's worth spending some time reading this section before making a decision.

Setuptools
^^^^^^^^^^

The default packaging system for the Python Template (and for Python, in general) is `setuptools <https://setuptools.readthedocs.io/en/latest/index.html>`__, i.e., the well-known ``setup.py`` file. We refer to `their documentation <https://setuptools.readthedocs.io/en/latest/setuptools.html>`__ for details on how the system works.

Starting with version 30, setuptools provides the option of using a ``setup.cfg`` file to consolidate all the necessary information for packaging, that used to be distributed across multiple files. ``setup.cfg`` includes the package metadata (its name, which matches the ``repo_name`` defined when initialising the product, version, author name and email, keywords, URLs, etc) but also the dependencies (which used to be included in ``requirements`` files), and package data (the ``MANIFEST.in`` file), etc.

The ``setup.cfg`` provided with the template is a ready-to-deploy file which includes both the production and development dependencies. We also include sensible configurations for many tools such as `isort <https://github.com/timothycrosley/isort>`__, `flake8 <https://coverage.readthedocs.io/>`__ `pytest <https://pytest.org/>`__, `coverage <https://coverage.readthedocs.io/>`__, etc. Using a ``setup.cfg`` dramatically reduces the number of files needed to configure your package and makes it easier to know where to go to change a parameter.

To install your package, just run ``pip install .`` or (less preferred) ``python setup.py install``.

Poetry
^^^^^^

Until recently, setuptools and its deprecated predecessor, `distutils <https://docs.python.org/3/library/distutils.html>`__, were the only options for packaging and publication of Python products. This has changed with the publication of `PEP-517 <https://www.python.org/dev/peps/pep-0517/>`__ and `PEP-518 <https://www.python.org/dev/peps/pep-0518/>`__, which define a framework for creating custom build systems that can still be used with pip and PyPI. While the implementation of these standards is still incomplete, their publication opened the door for a number of new build frameworks that aim to address several shortcomings in setuptools.

One such build system is `poetry <https://python-poetry.org/>`__. poetry aims to provide a better development environment, integrating virtual environments with a robust dependency resolution.

The Python ecosystem is very large and somehow convolved, with packages depending on each other in sometimes complicated and conflicting ways. Say, for example, that you have a package ``projectA`` that dependes on ``projectB>=1.0.0`` and ``projectC>=2.0.0`` but it also happens that ``projectB`` depends on ``projectC<2.0.0``. This is obviously a conflict and it should not be possible to publish ``projectA`` in such way. setuptools and pip provide ways to define the previous dependency versions but they are quite bad at making sure that all the dependencies are coherent: their purpose is to install the requested products, not to look for conflicts.

In the case above, if you pip install ``productB==2.1.2``, it will also install ``productC==1.1.1``. But if you now install ``productC==2.7.1``, that won't change the already installed ``productB``. Depending on the order of the installations you may see a warning while running pip, but you have ended up with a broken dependency tree. This is even more likely to happen if you are not using a dedicated virtual environment for development.

Poetry tries to avoid that by always installing dependencies in a virtual environment (and making it easy to manage) and by running a dependency resolution algorithm on each new dependency. If the dependency versions you are trying to use conflict, as in the earlier example, poetry will uncompromisingly prevent you from adding the new dependency.

Now that we have examined the motivations, let's see how poetry works. PEP-517 defines a new file ``pyproject.toml`` to store the metadata and dependencies. Similar to ``setup.cfg``, the template provides a flight-ready ``pyproject.toml`` for the cookiecut project, along with configurations for tools such as flake8, pytest, etc. To add a new dependency, one simple does ::

    poetry add <new-dependency>

and, if there are no conflicts, the dependency is added to ``pyproject.toml``. There are two sections for production dependencies and development ones. The poetry build system does not use a ``setup.py`` file. Instead, the build backend is defined in the ``[build-system]`` section of ``pyproject.toml``. You can still do ``pip install .`` or ``pip install sdss-mypackage`` and pip will know to use poetry to install your product.

In addition to these core components, poetry provides a number of nice features such as easy packaging and publication to PyPI, version bumping, etc. We refer to `its documentation <https://python-poetry.org/docs/>`__ for details.

At the time of this writing, poetry has reached version 1.0.0 and is quite stable, but there are some features still missing. The main caveats to consider when thinking about adopting poetry are:

- Poetry does not allow to do editable install with ``pip install -e .`` (although doing ``poetry install`` does an editable install of your product, more on this in the :ref:`developing-section-v2` section).

- Poetry does not provide a good build system for `extensions <https://docs.python.org/3/extending/building.html>`__ (e.g., Cython).

The first issue is caused by the incomplete implementation of PEP-517 in pip and it can be expected to be fixed at some point during 2020. The second is expected to be addressed by poetry itself at some point (note that there is a `workaround <https://github.com/python-poetry/poetry/issues/11>`__ to build extensions, but it comes with some caveats).

To deal with these issues, the Python Template provides a ``create_setup.py`` script that generates a ``setup.py`` file based on the poetry information. We talk about it in detail in the :ref:`developing-section-v2` section.


.. _tools-section-v2:

Tools
-----

The template comes with some tools for logging, configuration parsing, version management, and task handling. In version 1 of the template these code for these tools was included with the template. This was suboptimal because any bug fixes or improvements to those tools could not be propagated to already cut projects. If, for example, a bug was discovered in the logging tool, you'd need to manually modify each of your cookiecut products to fix it.

For version 2 we have moved those tools to a small, external repository called `sdsstools <https://github.com/sdss/sdsstools>`__. The template depends on it to provide these features so that if ``sdsstools`` gets update, you can simply do ``pip install --upgrade sdsstools`` and get all any new feature or bug fix. You can also use ``sdsstools`` for any project, even if it's not derived from this template.

Normally, ``sdsstools`` will be installed as part of the cookiecut process, but depending on your Python installation and whether you are using virtual environments you may need to manually pip install it.

.. _versioning-section-v2:

Version management
^^^^^^^^^^^^^^^^^^

:ref:`Version 1 <bumpversion-section-v1>` of the template used `bumpversion <https://github.com/peritus/bumpversion>`__ for version bumping. ``bumpversion`` is, however, not totally trivial to use, and the project has been abandoned.

In version 2 we simplify the process of handling the version of your product by using the `sdsstools.metadata <https://github.com/sdss/sdsstools#metadata>`__ module. The version of the product is defined *only* in your ``pyproject.toml`` or ``setup.cfg``. The cookiecut template uses the ``sdsstools.get_package_version`` function to determine the version and stores it in the ``__version__`` attribute so you can do ::

    >>> from mypackage import __version__
    >>> print(__version__)
    0.1.0-alpha.0

To modify or bump the version, just go to the ``pyproject.toml`` or ``setup.cfg`` file and change it manually. Or, if using poetry, you can use `poetry version <https://python-poetry.org/docs/cli/#version>`__.

The :ref:`Sphinx documentation <sphinx-section-v2>` includes a `substitution <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#substitution-definitions>`__, ``|mypackage_version|`` that you can use anywhere in your rST files to include the product version.

.. _conf-log-section-v2:

Configuration file and logging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Available levels are ``.debug``, ``.info``, ``.error``, and ``.critical``. For warnings, use the `warnings <https://docs.python.org/3/library/warnings.html>`__ module. Warnings will be redirected to all the available logging handlers after being formatter and coloured.

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

The logging and configuration features are provided by the modules `sdsstools.logger <https://github.com/sdss/sdsstools#logging>`__ and `sdsstools.configuration <https://github.com/sdss/sdsstools#configuration>`__, respectively.

.. _tasks-section-v2:

Using tasks
^^^^^^^^^^^

``sdsstools`` comes with a command line script, ``sdss`` that you can call from anywhere. This CLI is a simple wrapper around a series of `Invoke <http://www.pyinvoke.org/>`__ tasks. You can think of them as macros for frequently used operations.

If you run ``sdss`` you'll get a list of available tasks, such as :ref:`build documentation <sphinx-section-v2>`, or clean the workspace. A full list is available `here <https://github.com/sdss/sdsstools#command-line-interface>`__, and we'll mention them in the following sections.

Note that the CLI requires ``sdsstools`` to be installed for development ::

    pip install sdsstools[dev]

Currently there is no procedure to extend the list of tasks in ``sdsstools``, but you can always create your own ``tasks.py`` file on the root of the project and use Invoke natively.


.. _deploying-section-v2:

Deploying your product
----------------------

This section explains how to deploy a new version of your product to `PyPI <https://pypi.python.org/pypi>`_ so that it becomes `pip <https://pip.pypa.io/en/stable/>`_-installable.

The first step is to make sure that your project is ready to be deployed. This includes checking that the version is correct (i.e., not a pre-release or beta) and tagging the product. If using poetry, you may want to run a final ``poetry update`` to make sure all dependencies are correct.


Next, you will need to create a ``~/.pypirc`` file with the following content ::

    [distutils]
    index-servers=
    pypi

    [pypi]
    repository = https://pypi.python.org/pypi
    username = [username]
    password = [password]

Here you have two options; you can either use your own account in PyPI to deploy the product, or use the SDSS one. For the latter, you'll need to ask for the username and password by emailing ``admin[at]sdss[dot]org``. If you use your own account, and after the new project has been created, remember to go to the management options and make ``sdss`` an **owner** of the project. This will allow other people in SDSS to edit it or contribute new versions if you stop being a maintainer.

To deploy a new release you will need `twine <https://pypi.python.org/pypi/twine>`_. To install it ::

    pip install twine

Then, from the root of your product, run ::

    sdss deploy

which will create source and `wheel <https://pythonwheels.com/>`_ distributions of your package and upload them to PyPI. The command above is equivalent to running ::

    python setup.py sdist bdist_wheel --universal
    twine upload dist/*

The ``pip_name`` that you selected when you cookiecut the new project specifies the name of the package as it appears in PyPI and how it will be installed.  To avoid potential conflicts with existing packages, all SDSS package pip-names should adhere to the format ``sdss-[pkgname]``.  E.g. the Python package ``tree`` would be called ``sdss-tree``.  The python package ``sdss_access`` would be called ``sdss-access``.

If you are using poetry this procedure may fail so it's better to use poetry's own publication system. Simply do ::

    poetry build
    poetry publish

which are equivalent to the build and upload steps above.


.. _tests-section-v2:

Writing and running tests
-------------------------

The ``tests`` directory contains some examples on how to write and run tests for your package using `pytest`_. Use the `conftest.py <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.package_name%7D%7D/tests/conftest.py>`__ file to define `fixtures <https://docs.pytest.org/en/latest/fixture.html>`__ and other `pytest`_-specific features. cd'ing to the ``tests`` directory and typing ``pytest`` will recursively run all the tests in files whose filename starts with ``test_``.

If you prefer to use `unittest <https://docs.python.org/3/library/unittest.html>`_ or `nose <https://nose2.readthedocs.io/en/latest/getting_started.html>`_ feel free to remove those files.

.. _travis-section-v2:

Connecting your product to Travis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The template includes a basic setup for `Travis CI <https://travis-ci.org/>`__ and `codecov <https://codecov.io>`_. The configuration is defined in the `.travis.yml <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.package_name%7D%7D/.travis.yml>`__. `Coverage <https://coverage.readthedocs.io/>`__ configuration is included in your ``pyproject.toml`` or ``setup.cfg`` files.

Once you have created the GitHub repository for the product, you can go to your `Travis CI <https://travis-ci.org>`__ account (create one if you don't have it) and click on ``Add a new repository``. Then search for the new product and flip the switch to initiate the integration. You can do the same for codecov_. Each new push to the repository will trigger a Travis run that, if successful, will update the coverage report (to see it, you will also need to go to to codecov_, sign with your GitHub account, and turn on the repository).


.. _sphinx-section-v2:

How to build Sphinx Documentation
---------------------------------

This template includes `Sphinx <http://www.sphinx-doc.org/en/stable/>`_ documentation, written using the `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ format.  The documentation is located inside your python package, in a ``docs/sphinx/`` directory.  You can build the existing Sphinx documentation using invoke ::

    sdss docs.build

Alternatively, navigate to your python package's ``docs/sphinx/`` directory and type ::

    make html

This will build your documentation, converting the rst files into html files.  The output html files live in the ``docs/sphinx/_build`` subdirectory.  To both build and display the documentation, type::

    # builds and displays
    sdss docs.show

The main page of your documentation lives at ``docs/sphinx/_build/html/index.html``.  New documentation must be written in the rst syntax for Sphinx to understand and properly build html files.

The template includes an example on how to automatically document the docstrings in your code. In ``docs/sphinx/api.rst`` you'll see the lines ::

    .. automodule:: mypython.main
       :members:
       :undoc-members:
       :show-inheritance:

You can add similar blocks of code for other modules. See the Sphinx `autodoc <http://www.sphinx-doc.org/en/stable/ext/autodoc.html>`_ for more details. The :ref:`coding standards <style-docstring>` include a section on how to write good docstrings to document your code.

.. _rtd-section-v2:

Connecting your product to Read The Docs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The cookiecut product documentation is ready to be built and integrated with Read The Docs. As with Travis and Coveralls above, you will need to commit the products to a GitHub repository first. As with PyPI, SDSS has a `Read The Docs <http://readthedocs.io/>`__ account to which you can request access by emailing ``admin[at]sdss[dot]org``. Alternatively, you can deploy your product in your own Read the Docs account and add the user ``sdss`` as a maintainer from the admin menu. The expected address of your documentation will be ``https://<pip_name>.readthedocs.org``.

You may receive a message saying that the integration of the product is not complete and that you need to set up a webhook. To do that, got to the admin setting of the new Read The Docs project. In ``Intergations`` add a new integration and copy the link to the webhook. Then go to the GitHub repository settings and in the ``Webhooks`` section add a new webhook with the URL you just copied. Once you submit, any push to the master branch of the GitHub repo should produce a new built of the documentation. You can find more details on the webhook set up `here <https://docs.readthedocs.io/en/latest/webhooks.html>`_.

The product configuration for Read The Docs can be found in `readthedocs.yml <https://github.com/sdss/python_template/blob/master/%7B%7Bcookiecutter.package_name%7D%7D/readthedocs.yml>`_. By default, the Sphinx documentation will be built using Python 3.7 and will install the product with all its production requirements. If you have dependencies that are needed only for building the documentation (for example, a custom Sphinx theme), your can add them to the ``docs`` extras section of ``pyproject.toml`` or ``setup.cfg``.


.. _sdsspy-v2:

SDSS tree and sdss_access
-------------------------

This template includes the SDSS `tree <http://github.com/sdss/tree>`__ and `sdss_access <http://github.com/sdss/sdss_acess>`__ Python packages.  This template adds these products as required dependencies in your installed project's `requirements.txt` file.  We encourage you to use these packages inside your code.  The ``tree`` package is designed to set up the SDSS SAS environment system dynamically within your Python environment.  The ``sdss_access`` package is designed to provide local and remote filesystem path generation and downloading.  To use these yourself, you may need to install them::

    pip install sdss-tree
    pip install sdss-access

See the `tree <http://sdss-tree.readthedocs.io/en/latest/>`__ and `sdss_access <http://sdss-access.readthedocs.io/en/latest/>`__ `readthedocs` for full documentation on each package, but in brief, to use the ``tree``::

    # loads the full SAS using the sdsswork configuration.  You only need to do this one per Python session.
    from tree import Tree
    my_tree = Tree()

and to use ``sdss_access``::

    # generate a local path to a file
    from sdss_access.path import Path
    path = Path()
    filepath = path.full('mangacube', drpver='v2_3_1', plate='8485', '1901')


.. _developing-section-v2:

Developing your product
-----------------------

Now that we have seen what's included with your new product, how should you develop it? This, of course, depends on your habits and preferences, but here we list a few good advice.

The most important thing to do is to **always develop your product in a virtual environment**. You can use `virtualenv <https://virtualenv.pypa.io/en/latest/>`__ or `pyenv <https://github.com/pyenv/pyenv>`__ to create and activate a new environment for your new product. This makes sure that you don't have conflicting products installing dependencies: for example, assume that your package needs ``numpy`` but numpy is already present in your global installation of Python; because all your ``import numpy`` work you may forget about it and not add it as dependency.

In general, if working on a project that only depends on other Python products, you should not need to use modules or set the ``PYTHONPATH`` variable. Those are only necessary if you depend on non-Python products (for example, an IDL product, or a configuration directory).

While working on a virtual environment, every time you install a new package remember to also add it to ``pyproject.toml`` or ``setup.cfg``, making sure you define the version ranges correctly. If you are using poetry, things are simpler since poetry enforces the use of a virtual environment; in that case just run ``poetry add <dependency>`` and it will be added to ``pyproject.toml``.

It is a good practice to set up Travis early on during your project development. Each Travis run is executed on an isolated environment so, in addition of running your tests on each commit, you may find issues with your dependency declaration that way.

Sometimes you'll be developing on several project at the same time, each one depending on some of the others. In that case `pip editable installs <https://stackoverflow.com/questions/35064426/when-would-the-e-editable-option-be-useful-with-pip-install>`__ can be useful. By doing ::

    pip install -e <path-to-projectB>

you can make ``projectB`` available to your project A, but if you make changes directly in ``<path-to-projectB>``, those changes will reflect also in ``projectA`` without having to run pip install again.

Considerations when using poetry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Poetry provides a very nice framework for development but comes with some caveat and frequent confusions. When you run ``poetry install`` you product will be installed in the virtual environment as an *editable install*. This means that if you then change the code, you can see the results without having to install it again.

Remember that after doing ``poetry install`` you either need to activate the virtual environment to run commands such as ``pytest`` or do ``poetry run pytest`` to make sure the command is execute inside the product environment.

When you run ``poetry install`` or ``poetry add``, a `poetry.lock file <https://python-poetry.org/docs/basic-usage/#installing-dependencies>`__ is generated. This file contains the exact versions that are installed in your environment and *you must commit it*. When you run ``poetry install`` with the lock file present, poetry install those specific version, providing a method to define a completely reproducible environment. If you want to update the versions of your dependencies (always with the constrains defined in ``pyproject.toml``) you can do ``poetry update``, which will also update the lock file.

The main caveat when working with poetry has to do with the incomplete implementation of PEP-517 in pip. Because of that, you cannot do pip editable installs on your poetry product with ``pip install -e .`` (note that you **can** do ``pip install .`` for a normal installation).

The second caveat is that the build system for C extensions is quite experimental at this point, as described :ref:`here <poetry-extensions>`.

To solve both those issues you may want to manually generate a ``setup.py`` file with the build information. The template provides a ``create_setup.py`` script that uses poetry itself to generate the ``setup.py``. If you do this, you need to run the script after each change to ``pyproject.toml`` or when you run a ``poetry add`` command. Remember to commit the ``setup.py`` file and treat it as a lock file.

In this case, you may also want to comment the following lines in ``pyproject.toml``

.. code-block:: toml

    [build-system]
    build-backend = "poetry.masonry.api"
    requires = ["poetry>=1.0.0"]

This will tell pip to not use poetry for installations, and instead use the ``setup.py`` with setuptools. You can still continue developing and deploying you code with poetry; this is only relevant for how other users will install your software.


How to modify this template
---------------------------

This template is built using `Cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_.  To add content to or expand this template, you must first check out the main template product using git::

    git clone https://github.com/sdss/python_template

Now you have the development version of this template.  The two main components need are a `cookiecutter.json` file and a `{{cookiecutter.package_name}}` directory.  Cookiecutter templates use the `Jinja2 <http://jinja.pocoo.org/docs/2.10/>`_ templating language to define variable substitution, using double bracket notation, e.g. `{{variable_name}}`.  All customizable content to be inserted by the user is defined using this notation.

* **{{cookiecutter.package_name}}**: the top-level directory defining the installed python package.  Everything below this directory belongs to the Python package that gets installed by the user.
* **cookiecutter.json**: A JSON file containing a dictionary of key:value pairs of variables defined in the template, with their default values.  These keys are referenced throughout the template with `{{cookiecutter.key}}`.

Upon installation of the template by a user, the variables defined in the `cookiecutter.json` file, or by the user during install, get substituted into their respective reference places.

Please, *do not* modify the master branch directly unless otherwise instructed. Instead, develop your changes in a branch or fork and, when ready to merge, create a pull request.


.. _faq-section-v2:

Frequently Asked Questions
--------------------------

**How do I install the just the requirement packages from setup.cfg?**

    Normally you'll want to install your package along with its requirements by doing ``pip install .`` (or, in editable mode, ``pip install -e .``). But what if you only want to install the dependencies but not the main product. In that case you can still do ``pip install .`` and then ``pip uninstall <mypackage>``, which will leave the dependencies installed.

    Alternatively, you can use the ``sdss install-deps`` :ref:`task <tasks-section-v2>` to install only the dependencies. You can even pass an ``--extras`` flag to tell it to install extras, for example ::

        sdss install-deps --extras dev,docs

.. _poetry-extensions:

**What if I need to build C/C++ extensions with poetry?**

    Poetry provides a fairly immature system to build extensions. You can add your extensions to a file called ``build.py`` and then tell ``pyproject.toml`` to use it for extension building. See `this thread <https://github.com/python-poetry/poetry/issues/11>`__ for details. The template already includes a placeholder ``build.py``; just add your `Extension <https://docs.python.org/3.8/library/distutils.html>`__ instances there. Note that, as discussed :ref:`here <developing-section-v2>`, this will require using the ``create_setup.py`` script and handling the generated ``setup,py`` as a lock file.


.. toctree::
    :hidden:

    v1/v1
    standards
    changelog
