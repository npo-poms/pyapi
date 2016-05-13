#!/usr/bin/env python3
from distutils.core import setup

__version__ = None
exec(open('npoapi/_version.py', "rt").read())

setup(
    name='NPO API',
    version=__version__,
    packages=['npoapi', 'npoapi.xml' ],
    scripts=[
        'bin/npo_media_get',
        'bin/npo_media_search',
        'bin/npo_pages_get',
        'bin/npo_pages_search',
        'bin/npo_media_changes',
        'bin/npo_schedule_get',
        'bin/npo_check_credentials',
        'bin/npo_mediabackend_get'
        ],
    long_description=open('README.txt').read(),
)
