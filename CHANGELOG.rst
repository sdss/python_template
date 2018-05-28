.. _python-template-changelog:

==========
Change Log
==========

This document records the main changes to the python-template code.

.. _changelog-master:

master
------

Added
^^^^^
* Added W0621 to diabled list in pylint.

Changed
^^^^^^^
* Changed documentation font size.
* Modified code and readthedocs configuration to use Python 3.6.
* Better logging of warnings. Logger is defined inside the custom warnings to prevent ``warnings.showwarnings`` from being overwritten.

Fixed
^^^^^
* Problem importing matplotlib in docs.
* A typo in the definition of the warning format in the logger.
* A typo in the definition of the API exception.

`View commits <https://github.com/sdss/python_template/compare/1.0.0...HEAD>`__


.. _changelog-1.0.0:

1.0.0 (2018-01-31)
------------------

Added
^^^^^
* Initial release.
* Includes Travis CI, Read The Docs, Coverage, and Bumpversion integrations.
* Includes a logger and configuration library.
* Examples for Sphinx documentation and pytest.

`View commits <https://github.com/sdss/python_template/compare/b726b904a601fe051b9db8dfd24fee59f70bc866...1.0.0>`__
