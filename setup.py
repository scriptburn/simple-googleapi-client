
"""Setup script for Google API Python client.
Also installs included versions of third party libraries, if those libraries
are not already installed.
"""
from __future__ import print_function

import sys

 

from setuptools import setup

packages = [
    'simplegoogleapi'
]

install_requires = [
    'google-api-python-client>=1.7.9'
]

long_desc = """A simple wrapper for google-api-python-client."""

import simplegoogleapi
version = simplegoogleapi.__version__

setup(
    name="simple-googleapi-client",
    version=version,
    description="A simple wrapper for google-api-python-client.",
    long_description=long_desc,
    author="Rajneesh ojha",
    author_email="rajneeshojha123@gmail.com",
    url="https://github.com/scriptburn/simple-googleapi-client",
    install_requires=install_requires,
    packages=packages,
    package_data={},
    license="Apache 2.0",
    keywords="simple googleapi client",
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)