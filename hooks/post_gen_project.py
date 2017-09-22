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

CURRENTDIR = os.path.abspath(os.curdir)
PYTHONDIR = os.path.join(CURRENTDIR, 'python')


@invoke.task
def install(ctx):
    ''' Cleans and installs the new repo '''

    os.chdir(CURRENTDIR)
    print('Installing {0}'.format(PKGNAME))
    ctx.run("python setup.py clean")
    ctx.run("python setup.py install")


pyinstall = '{{ cookiecutter.install_package_at_end }}'
if pyinstall in ['yes', 'y']:
    if invoke:
        col = invoke.Collection(install)
        ex = invoke.executor.Executor(col)
        ex.execute('install')
else:
    print('Please add {0} into your PYTHONPATH!'.format(PYTHONDIR))

