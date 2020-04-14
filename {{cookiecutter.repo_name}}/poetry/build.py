#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2019-12-17
# @Filename: build.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

# Extension build system using poetry, see https://github.com/python-poetry/poetry/issues/11.
# Add your Extension modules (https://docs.python.org/3.8/library/distutils.html) to the
# ext_modules list and they will be build and installed on poetry install.
# For production, you will need to use the create_setup.py script to manually
# generate a setup.py or the installation will fail because of the lack of
# setup.py. This is a bug in poetry that hopefully will be fixed soon.


ext_modules = [
]


def build(setup_kwargs):
    """To build the extensions with poetry."""

    setup_kwargs.update({
        'ext_modules': ext_modules
    })
