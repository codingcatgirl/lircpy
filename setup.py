#!/usr/bin/env python3
import os

from setuptools import setup

setup(
    name='lircpy',
    version='0.1.0',
    description='accessing the LIRC socket interface using Python 3',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    packages=['lircpy'],
    py_modules=['lircpy'],
    author='Laura Klünder',
    author_email='lircpy@codingcatgirl.de',
    url='https://github.com/codingcatgirl/lircpy',
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
