# tor2torrent [![Build Status](https://travis-ci.org/adolfosilva/tor2torrent.svg)](https://travis-ci.org/adolfosilva/tor2torrent)

tor2torrent is a Python 3 script to create bittorrent files for [Tor Project](https://www.torproject.org) packages.

> ***Note:*** This project is in no way officially associated with the Tor Project.

## Installation

If you have [setuptools](https://pypi.python.org/pypi/setuptools/) installed, simply do:

	$ sudo python setup.py install

## Usage

To create a torrent file for a specific package just give it its name as the argument.

```
$ python3 tor2torrent.py tor-0.2.6.1-alpha
Downloading: https://dist.torproject.org/tor-0.2.6.1-alpha.tar.gz
Downloading: https://dist.torproject.org/tor-0.2.6.1-alpha.tar.gz.asc
Creating torrent: tor-0.2.6.1-alpha.torrent
```

## Contributing

If you want to contribute to this project, just fork it and send me some pull requests.
Happy hacking!

## License

Both py3createtorrent and tor2project are licensed under the GPL 3.0 license. See LICENSE for details.

## Contact

You can contact me at `code@anomi.co`.
