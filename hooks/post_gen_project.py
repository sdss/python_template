# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#

from __future__ import print_function, division, absolute_import
import os
try:
    import invoke
except ImportError as e:
    invoke = None

#
# This script runs after the cookiecutter template has been installed
#
#

REPONAME = '{{ cookiecutter.repo_name }}'
PKGNAME = '{{ cookiecutter.package_name }}'

ROOTDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))


@invoke.task
def install(ctx):
    ''' Cleans and installs the new repo '''

    pkgdir = os.path.join(ROOTDIR, REPONAME)
    os.chdir(pkgdir)
    print('Installing {0}'.format(PKGNAME))
    ctx.run("python setup.py clean")
    ctx.run("sudo python setup.py install")
    os.chdir(ROOTDIR)


if invoke:
    invoke.tasks.Call(install)
