.. _python-template-changelog:

==========
Change Log
==========

This document records the main changes to the python-template code.

.. _python-template-master:

master
------

`View commits since the last tag <https://github.com/sdss/python_template/compare/1.0.6...HEAD>`__.


.. _python-template-1.0.6:

1.0.6 (2019-12-31)
------------------

Added
^^^^^
* Avoid connecting more than one console handler to the warnings log.

Fixed
^^^^^
* Do not modify the record when formatting it, in case that record is also output in other handlers.

`View commits <https://github.com/sdss/python_template/compare/1.0.5...1.0.6>`__.


.. _python-template-1.0.5:

1.0.5 (2019-05-13)
------------------

Backward incompatible changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* The default path for the user configuration file is now ``~/.config/<name>/<name>.yml``.

Added
^^^^^
* Better handling of configuration files. An environment variable ``$<NAME>_CONFIG_PATH`` (e.g., ``$MYPYTHON_CONFIG_PATH``) can be defined to point to the user configuration file. If defined, this path overrides the default location.

Changed
^^^^^^^
* Modified logger to deal with warnings. Added critical level printing. Fixes :issue:`12,13`.

Fixed
^^^^^
* Bug causing Python 2.7 templates to fail because ``PercentStyle`` is not available in ``logging`` module (thanks to :user:`andycasey`).

`View commits <https://github.com/sdss/python_template/compare/1.0.4...1.0.5>`__.


.. _python-template-1.0.4:

1.0.4 (2019-01-18)
------------------

Changed
^^^^^^^
* Updated year in template to 2019.

Fixed
^^^^^
* More fixes to quotes in ``module-whatis`` in module file.

`View commits <https://github.com/sdss/python_template/compare/1.0.3...1.0.4>`__.


.. _python-template-1.0.3:

1.0.3 (2018-12-10)
------------------

Fixed
^^^^^
* Quotes in ``module-whatis`` in module file.

`View commits <https://github.com/sdss/python_template/compare/1.0.2...1.0.3>`__.


.. _python-template-1.0.2:

1.0.2 (2018-10-01)
------------------

Fixed
^^^^^
* Remove ``from __future__ import unicode_literals`` that made the package install fail under Python 2. See `#9 <https://github.com/sdss/python_template/issues/9>`__ for details.

`View commits <https://github.com/sdss/python_template/compare/1.0.1...1.0.2>`__.


.. _python-template-1.0.1:

1.0.1 (2018-07-30)
------------------

Added
^^^^^
* Added W0621 to disabled list in pylint.

Changed
^^^^^^^
* Changed documentation font size.
* Modified code and readthedocs configuration to use Python 3.6.
* Remove logger warning monkeypatching since it conflicted when used with packages that provide a similar monkeypatching. Replaced with a custom ``logging.warning`` method that produces coloured warning output.
* The ``package_name`` specified when cookiecutting the template is applied in lowercase when creating the package but in ucfirst case when creating classes.
* Renamed ``misc`` to ``utils``.

Fixed
^^^^^
* Problem importing matplotlib in docs.
* A typo in the definition of the warning format in the logger.
* A typo in the definition of the API exception.

`View commits <https://github.com/sdss/python_template/compare/1.0.0...1.0.1>`__.


.. _python-template-1.0.0:

1.0.0 (2018-01-31)
------------------

Added
^^^^^
* Initial release.
* Includes Travis CI, Read The Docs, Coverage, and Bumpversion integrations.
* Includes a logger and configuration library.
* Examples for Sphinx documentation and pytest.

`View commits <https://github.com/sdss/python_template/compare/b726b904a601fe051b9db8dfd24fee59f70bc866...1.0.0>`__.
