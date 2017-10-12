# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#

from __future__ import print_function, division, absolute_import
import os
import invoke

#
# This script runs after the cookiecutter template has been installed
#
#

GITUSER = '{{ cookiecutter.github_username }}'
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


@invoke.task
def addgit(ctx):
    ''' Cleans and installs the new repo '''

    os.chdir(CURRENTDIR)
    print('Initializing git repo {0}'.format(REPONAME))
    ctx.run("git init .")
    ctx.run("git add .")
    ctx.run("git commit -m 'Initial skeleton.'")
    addgithub = '{{cookiecutter.add_to_github}}'
    if addgithub in ['yes', 'y']:
        ctx.run("git remote add origin git@github.com:{0}/{1}.git".format(GITUSER, REPONAME))
        try:
            print('Pushing to github ..')
            ctx.run("git push -u origin master")
        except Exception as e:
            print('Could not push to github.  ERROR: Repository not found.')


col = invoke.Collection(install, addgit)
ex = invoke.executor.Executor(col)


# run python setup.py install or not
pyinstall = '{{ cookiecutter.install_package_at_end }}'
if pyinstall in ['yes', 'y']:
    ex.execute('install')
else:
    print('Please add {0} into your PYTHONPATH!'.format(PYTHONDIR))


# setup intial git repo
creategit = '{{ cookiecutter.create_git_repo }}'
if creategit in ['yes', 'y']:
    ex.execute('addgit')
