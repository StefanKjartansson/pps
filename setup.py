#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


is_py3k  = sys.version_info >= (3, 0)

if os.path.exists("README.rst"):
    long_description = codecs.open("README.rst", "r", "utf-8").read()
else:
    long_description = "No description"


required = []
entry_points = {}


setup(
    name = "{{name}}",
    version = "{{version|default('0.1')}}",
    packages = find_packages(),
    install_requires = required,
    author="{{author.name}}",
    author_email="{{author.email}}",
    description="{{description}}",
    long_description=long_description,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    entry_points=entry_points,
    zip_safe=False,
)
