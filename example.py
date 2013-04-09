#!/usr/bin/env python3

import sys
import pprint
import os
import bencode


if len(sys.argv) != 2:
    print("Usage: example.py torrentfile.torrent")

with open(sys.argv[1], 'rb') as fh:
    torrent_bytes = fh.read()

torrent = bencode.decode(torrent_bytes)
outfilename = os.path.splitext(sys.argv[1])[0] + ".txt"

with open(outfilename, 'w') as fh:
    fh.write(pprint.pformat(torrent))


