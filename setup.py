#!/usr/bin/env python3
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='enocean_async',
    version='1.0.2',
    author='Angelo Cutaia',
    author_email='angeloxx92@hotmail.it',
    description='EnOcean serial protocol async implementation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Angeloxx92/enocean_async',
    packages=[
        'enocean_async',
        'enocean_async.protocol',
        'enocean_async.communicators',
    ],
    scripts=[
        'examples/enocean_example.py',
    ],
    package_data={
        '': ['EEP.xml']
    },
    install_requires=[
        'enum-compat>=0.0.2',
        'pyserial-asyncio>=0.4',
        'beautifulsoup4>=4.3.2',
        'aioconsole>=0.1.15',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
    )
