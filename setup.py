"""
setup.py configuration script describing how to build and package this project.

This file is primarily used by the setuptools library and typically should not
be executed directly. See README.md for how to deploy, test, and run
the dabs_poc project.
"""
from setuptools import setup, find_packages

import sys
sys.path.append('./src')

import datetime
import dabs_poc

setup(
    name="dabs_poc",
    version=dabs_poc.__version__ + "+" + datetime.datetime.utcnow().strftime("%Y%m%d.%H%M%S"),
    url="https://databricks.com",
    author="cfuentes@thoughtworks.com",
    description="wheel file based on dabs_poc/src",
    packages=find_packages(where='./src'),
    package_dir={'': 'src'},
    entry_points={
        "packages": [
            "main=dabs_poc.main:main"
        ]
    },
    install_requires=[
        "setuptools"
    ],
)
