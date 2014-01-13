from __future__ import unicode_literals

import re
from setuptools import setup, find_packages


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-Ferguson',
    version=get_version('mopidy_ferguson/__init__.py'),
    url='https://github.com/mattbrailsford/mopidy-ferguson',
    license='Apache License, Version 2.0',
    author='Matt Brailsford',
    author_email='me@mattbrailsford.com',
    description='Mopidy extension to control Mopidy by GPIO connected controls',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 0.17',
        'Pykka >= 1.1',
    ],
    entry_points={
        'mopidy.ext': [
            'ferguson = mopidy_ferguson:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)