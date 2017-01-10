#!/usr/bin/env python
# -*-encoding:utf8-*-
from setuptools import setup

setup(
    name='eyes',
    version='1.0',
    py_modules=['monitor'],
    install_requires=[
        'Click',
    ],
    entry_points='''
       [console_scripts]
       eyes=monitor:start
    ''',
)
