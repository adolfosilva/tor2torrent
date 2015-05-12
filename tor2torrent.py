#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Script to create bittorrent files for Tor Project packages."""

import os
import sys
import shutil
import argparse
import requests

__author__    = 'Adolfo Silva <code@anomi.co>'
__license__   = 'GPL'
__version__   = '0.1.0'

dist = 'https://dist.torproject.org/'

def remove_targz(name):
   return name.split('.tar.gz')[0]

def add_targz(name):
   return name + '.tar.gz'

def download_package(name):
   with open(name, 'wb') as f:
      path = dist+name
      print('Downloading: ' + path)
      f.write(requests.get(path).content)

def download_signature(name):
   with open(name+'.asc', 'wb') as f:
      path = dist+name+'.asc'
      print('Downloading: ' + path)
      f.write(requests.get(path).content)

def create_torrent(name, verbose=False):
   print('Creating torrent: ' + name+'.torrent')
   if not verbose:
      os.system('python3 py3createtorrent-0.9.5/py3createtorrent.py -q --md5 -c "" -d -1 -n %s %s ccc publicbt openbt' % (name, name))
   else:
      os.system('python3 py3createtorrent-0.9.5/py3createtorrent.py --md5 -c "" -d -1 -n %s %s ccc publicbt openbt' % (name\
, name))

def make_directory(name):
   if not os.path.exists(name):
      os.makedirs(name)

def move_package_and_signature_to_dir(name):
   os.system('mv %s %s %s/' % (add_targz(name), add_targz(name)+'.asc', name))

def mirror_website(url):
   os.system('wget -mk ' + dist)

def setup_argument_parsing():
   parser = argparse.ArgumentParser(description='bittorrent creation for Tor Project packages ')
   parser.add_argument('name', type=str, help='name of the package')
   parser.add_argument('-v', '--verbose', action='store_true', help='be verbose')
   return parser.parse_args()

def delete_directory(path):
   shutil.rmtree(path)

def main():
   args = setup_argument_parsing()
   name = args.name
   targz = add_targz(name)
   # mirror_website(dist)
   # sys.exit(0)
   download_package(targz)
   download_signature(targz)
   make_directory(name)
   move_package_and_signature_to_dir(name)
   create_torrent(name, args.verbose)
   delete_directory(name)

if __name__ == '__main__':
    main()
