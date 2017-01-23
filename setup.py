#!/usr/bin/env python
# -*-encoding:utf8-*-
from setuptools import setup, find_packages

setup(
    name='eyes',
    version='1.0',
    description='app rank monitor',
    author='javasgl',
    url='https://github.com/javasgl/eyes',
    packages=find_packages(),
    py_modules=['monitor'],
    install_requires=[
        'Click',
        'pyquery'
    ],
    entry_points='''
       [console_scripts]
       eyes=monitor:start
    ''',
)
