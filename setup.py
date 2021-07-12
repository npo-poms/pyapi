#!/usr/bin/env python3
from setuptools import setup

__version__ = None
exec(open('npoapi/_version.py', "rt").read())

setup(
    name='NPO API',
    version=__version__,
    packages=['npoapi', 'npoapi.xml'],
    install_requires=[
        'pytz==2020.1',
        'ijson==3.1.2.post0',
        'pyxb==1.2.6',
        'python-dateutil==2.8.1',
        'jwt==1.0.0',
        'typing==3.7.4.3',
        'requests==2.25.1'
    ],
    scripts=[
        'bin/npo_media_get',
        'bin/npo_media_search',
        'bin/npo_media_iterate',
        'bin/npo_pages_get',
        'bin/npo_pages_search',
        'bin/npo_media_changes',
        'bin/npo_schedule_get',
        'bin/npo_schedule_search',
        'bin/npo_check_credentials',
        'bin/npo_mediabackend_get',
        'bin/npo_mediabackend',
        'bin/npo_pagesbackend',
        'bin/npo_thesaurus',
        'bin/npo_subtitles',
        'bin/npo_integration_tests'
    ],
    long_description=open('README.txt').read(),
)
