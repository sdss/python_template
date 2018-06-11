# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2017-12-05 12:01:21
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2017-12-05 12:19:32

from __future__ import print_function, division, absolute_import
{% set package_ucfirst = cookiecutter.package_name[0:1]|upper ~ cookiecutter.package_name[1:] %}

class {{package_ucfirst}}Error(Exception):
    """A custom core {{package_ucfirst}} exception"""

    def __init__(self, message=None):

        message = 'There has been an error' \
            if not message else message

        super({{package_ucfirst}}Error, self).__init__(message)


class {{package_ucfirst}}NotImplemented({{package_ucfirst}}Error):
    """A custom exception for not yet implemented features."""

    def __init__(self, message=None):

        message = 'This feature is not implemented yet.' \
            if not message else message

        super({{package_ucfirst}}NotImplemented, self).__init__(message)


class {{package_ucfirst}}APIError({{package_ucfirst}}Error):
    """A custom exception for API errors"""

    def __init__(self, message=None):
        if not message:
            message = 'Error with Http Response from {{package_ucfirst}} API'
        else:
            message = 'Http response error from {{package_ucfirst}} API. {0}'.format(message)

        super({{package_ucfirst}}APIError, self).__init__(message)


class {{package_ucfirst}}ApiAuthError({{package_ucfirst}}APIError):
    """A custom exception for API authentication errors"""
    pass


class {{package_ucfirst}}MissingDependency({{package_ucfirst}}Error):
    """A custom exception for missing dependencies."""
    pass


class {{package_ucfirst}}Warning(Warning):
    """Base warning for {{package_ucfirst}}."""


class {{package_ucfirst}}UserWarning(UserWarning, {{package_ucfirst}}Warning):
    """The primary warning class."""
    pass


class {{package_ucfirst}}SkippedTestWarning({{package_ucfirst}}UserWarning):
    """A warning for when a test is skipped."""
    pass


class {{package_ucfirst}}DeprecationWarning({{package_ucfirst}}UserWarning):
    """A warning for deprecated features."""
    pass
