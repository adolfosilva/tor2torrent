#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
from sys import version

SETUPTOOLS = False

try:
   from setuptools import setup
   SETUPTOOLS = False
except ImportError:
   from distutils.core import setup

if version < '2.2.3':
   from distutils.dist import DistributionMetadata
   DistributionMetadata.classifiers = None
   DistributionMetadata.download_url = None

def read(fname):
   return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='tor2torrent',
      version='0.1.0',
      description='Script to create bittorrent files for Tor Project packages',
      long_description=read('README.md'),
      author='Adolfo Silva',
      author_email='code@anomi.co',
      url='https://github.com/adolfosilva/tor2torrent',
      license='GPL',
)
