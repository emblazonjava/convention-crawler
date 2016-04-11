#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='ConventionCrawler',
    version='0.1',
    description='A tool for crawling a convention-over-configuration application and extracting knowledge about its structure.',
    author='Allison F',
    author_email='yetanotherallisonf@yahoo.com',
    url='https://github.com/allisonf/tic-tac-toe',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Quality Assurance',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(exclude=['docs', 'tests']),

   install_requires=["modgrammar"]
)