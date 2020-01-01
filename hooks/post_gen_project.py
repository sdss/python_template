# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.

import os
import shutil

import invoke
from invoke.exceptions import UnexpectedExit

#
# This script runs after the cookiecutter template has been installed
#

PACKAGING_SYSTEM = '{{ cookiecutter.packaging_system }}'

GITUSER = '{{ cookiecutter.github_organisation }}'
PIPNAME = '{{ cookiecutter.pip_name }}'
PKGNAME = '{{ cookiecutter.package_name }}'

CURRENTDIR = os.path.abspath(os.curdir)
PYTHONDIR = os.path.join(CURRENTDIR, 'python')


def copy_packaging_system():
    """Copies the appropriate files to use setup.cfg or poetry."""

    # Initially the repo is created with two directories, setup_cfg and poetry
    # that contain the files needed for each packaging system. Here, depending
    # on the cookiecutter configuration, we move the appropriate files and
    # remove the other ones.

    if PACKAGING_SYSTEM == 'setuptools':
        pack_dir = 'setup_cfg'
    elif PACKAGING_SYSTEM == 'poetry':
        pack_dir = 'poetry'
    else:
        raise ValueError(f'invalid packaging system {PACKAGING_SYSTEM!r}.')

    files = os.listdir(pack_dir)
    for file_ in files:
        shutil.move(os.path.join(pack_dir, file_), CURRENTDIR)

    # Delete both directories
    for dir_ in ['setup_cfg', 'poetry']:
        shutil.rmtree(dir_, ignore_errors=True)


@invoke.task
def install(ctx):
    ''' Cleans and installs the new repo '''

    os.chdir(CURRENTDIR)
    print('Installing {0}'.format(PKGNAME))
    ctx.run("python setup.py clean")
    try:
        ctx.run("python -d setup.py install", hide='both')
    except UnexpectedExit as e:
        print('Unexpected failure during install:\n {0}'.format(e.result.stderr))
        permden = '[Errno 13] Permission denied' in e.result.stderr
        if permden:
            print('Permission denied during install.  Trying again with sudo')
            ctx.run('sudo python -d setup.py install')


@invoke.task
def addgit(ctx):
    ''' Cleans and installs the new repo '''

    os.chdir(CURRENTDIR)
    print('Initializing git repo {0}'.format(PKGNAME))
    ctx.run("git init .")
    ctx.run("git add .")
    ctx.run("git commit -m 'Initial skeleton.'")


@invoke.task
def addremote(ctx):
    ''' Adds a new remote to your git repo and pushes to Github '''

    if GITUSER:
        ctx.run('git remote add origin https://github.com/{0}/{1}.git'
                .format(GITUSER, PKGNAME))
        try:
            print('Pushing to github ..')
            ctx.run("git push -u origin master")
        except Exception:
            print('Could not push to github. ERROR: Repository not found. '
                  'Make sure to add the repo to your github account. ')
    else:
        print('No GitHub username specified during setup')


@invoke.task
def install_sdsstools(ctx):
    """Tries to install sdsstools."""

    try:
        print('Installing sdsstools[dev]')
        ctx.run('pip install sdsstools[dev]')
    except Exception:
        print('Could install sdsstools. Try running '
              '"pip install sdsstools[dev]" manually.')


col = invoke.Collection(install, addgit, addremote, install_sdsstools)
ex = invoke.executor.Executor(col)

copy_packaging_system()
ex.execute('install_sdsstools')

# setup intial git repo
creategit = '{{ cookiecutter.create_git_repo }}'
if creategit in ['yes', 'y']:
    ex.execute('addgit')

# exists on Github?
exists_github = '{{ cookiecutter.exists_on_github }}'
if exists_github in ['yes', 'y']:
    ex.execute('addremote')


print('Please add {0} into your PYTHONPATH!'.format(PYTHONDIR))
