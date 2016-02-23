#!/usr/bin/env python3
import os

from setuptools import setup

setup(
    name='lircpy',
    version='0.1.0',
    description='accessing the LIRC socket interface using Python 3',
    packages=['lircpy'],
    py_modules=['lircpy'],
    author='Nicole Klünder',
    author_email='lircpy@nomoketo.de',
    url='https://github.com/NoMoKeTo/lircpy',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Home Automation'
    ],
    include_package_data=True
)
