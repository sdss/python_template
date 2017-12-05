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


class {{cookiecutter.package_name|title}}Error(Exception):
    """A custom core {{cookiecutter.package_name|title}} exception"""

    def __init__(self, message=None):

        message = 'There has been an error' \
            if not message else message

        super({{cookiecutter.package_name|title}}Error, self).__init__(message)


class {{cookiecutter.package_name|title}}NotImplemented({{cookiecutter.package_name|title}}Error):
    """A custom exception for not yet implemented features."""

    def __init__(self, message=None):

        message = 'This feature is not implemented yet.' \
            if not message else message

        super({{cookiecutter.package_name|title}}NotImplemented, self).__init__(message)


class {{cookiecutter.package_name|title}}ApiError({{cookiecutter.package_name|title}}Error):
    """A custom exception for API errors"""

    def __init__(self, message=None):
        if not message:
            message = 'Error with Http Response from {{cookiecutter.package_name|title}} API'
        else:
            message = 'Http response error from {{cookiecutter.package_name|title}} API. {0}'.format(message)

        super({{cookiecutter.package_name|title}}APIError, self).__init__(message)


class {{cookiecutter.package_name|title}}ApiAuthError({{cookiecutter.package_name|title}}APIError):
    """A custom exception for API authentication errors"""
    pass


class {{cookiecutter.package_name|title}}MissingDependency({{cookiecutter.package_name|title}}Error):
    """A custom exception for missing dependencies."""
    pass


class {{cookiecutter.package_name|title}}Warning(Warning):
    """Base warning for {{cookiecutter.package_name|title}}."""
    pass


class {{cookiecutter.package_name|title}}UserWarning(UserWarning, {{cookiecutter.package_name|title}}Warning):
    """The primary warning class."""
    pass


class {{cookiecutter.package_name|title}}SkippedTestWarning({{cookiecutter.package_name|title}}UserWarning):
    """A warning for when a test is skipped."""
    pass


class {{cookiecutter.package_name|title}}DeprecationWarning({{cookiecutter.package_name|title}}UserWarning):
    """A warning for deprecated features."""
    pass

