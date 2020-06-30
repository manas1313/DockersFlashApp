# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 01:58:08 2020

@author: routm1
"""

import setuptools
from appenv import infosetup


setup_info = infosetup.info()

#__name__= setup_info["name"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=setup_info["name"],
    version=setup_info["version"],
    author=setup_info["author"],
    author_email=setup_info["author_email"],
    description="This is a sample service for containerise",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
