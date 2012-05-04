#!/usr/bin/env python

from distutils.core import setup

execfile('package/version.py')

setup(
    name = 'TODO: Enter a name',
    version = __version__,
    description = 'TODO: Enter a description',
    long_description = open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
    author = 'TODO: Enter your name',
    author_email = 'TODO: Enter your e-mail address',
    url = 'TODO: Enter an URL',
    packages = [
        'TODO: Enter package(s)'
    ],
    classifiers = [
        'TODO: Add trove classifiers (http://pypi.python.org/pypi?%3Aaction=list_classifiers)'
    ]
)
