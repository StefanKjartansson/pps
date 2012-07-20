#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup file for {{name}}
"""
import codecs
import os
import sys

try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    raise
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages # noqa
    from setuptools.command.test import test # noqa


# Hack to prevent stupid "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when running `python
# setup.py test` (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing  # noqa
except ImportError:
    pass


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

long_description = read('README.rst')

required = []
entry_points = {}
tests_require = []

setup(
    author="{{author.name}}",
    author_email="{{author.email}}",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    description="{{description}}",
    entry_points=entry_points,
    install_requires=required,
    long_description=long_description,
    name="{{name}}",
    packages=find_packages(),
    version="{{version|default('0.1')}}",
    zip_safe=False,
    tests_require=tests_require,
    extras_require={'test': tests_require},
)
