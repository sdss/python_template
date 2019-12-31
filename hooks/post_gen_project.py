# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.

import os

import invoke
from invoke.exceptions import UnexpectedExit

#
# This script runs after the cookiecutter template has been installed
#

GITUSER = '{{ cookiecutter.github_username }}'
PIPNAME = '{{ cookiecutter.pip_name }}'
PKGNAME = '{{ cookiecutter.package_name }}'

CURRENTDIR = os.path.abspath(os.curdir)
PYTHONDIR = os.path.join(CURRENTDIR, 'python')


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


col = invoke.Collection(install, addgit, addremote)
ex = invoke.executor.Executor(col)


# setup intial git repo
creategit = '{{ cookiecutter.create_git_repo }}'
if creategit in ['yes', 'y']:
    ex.execute('addgit')

# exists on Github?
exists_github = '{{ cookiecutter.exists_on_github }}'
if exists_github in ['yes', 'y']:
    ex.execute('addremote')


print('Please add {0} into your PYTHONPATH!'.format(PYTHONDIR))
