#!/usr/bin/env python3
from distutils.core import setup

setup(
    name='NPO API',
    version='0.4dev',
    packages=['npoapi', ],
    scripts=[
        'bin/npo_media_get.py',
        'bin/npo_media_search.py',
        'bin/npo_pages_get.py',
        'bin/npo_pages_search.py',
        'bin/npo_media_changes.py',
        'bin/npo_schedule_get.py',
        'bin/npo_check_credentials.py'
        ],
    long_description=open('README.txt').read(),
)
