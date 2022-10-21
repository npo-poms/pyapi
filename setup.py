#!/usr/bin/env python3
from setuptools import setup, find_packages

__version__ = None
exec(open('npoapi/_version.py', "rt").read())

setup(
    name='NPO API',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'pytz==2021.3',
        'ijson==3.1.4',
        'pyxb==1.2.6',
        'python-dateutil==2.8.2',
        'jwt==1.3.1',
        'typing==3.7.4.3',
        'requests==2.26.0',
        'xsdata[cli]==22.9'
    ],
    scripts=[
        'bin/npo_media_get',
        'bin/npo_media_search',
        'bin/npo_media_iterate',
        'bin/npo_media_follow_changes',
        'bin/npo_pages_get',
        'bin/npo_pages_search',
        'bin/npo_pages_iterate',
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

    test_suite="nose.collector"

)
