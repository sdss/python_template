# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.

#
# This script runs before the cookiecutter template has been installed
#

# Checks that invoke is installed.

try:
    import invoke  # noqa
except ImportError:
    raise ImportError('cannot import invoke. Did you run \'pip install invoke\'?')
