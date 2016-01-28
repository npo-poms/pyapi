#!/usr/bin/env python3
from distutils.core import setup

setup(
    name='NPO API',
    version='0.3dev',
    packages=['npoapi', ],
    scripts=['bin/media_get.py'],
    long_description=open('README.txt').read(),
)
