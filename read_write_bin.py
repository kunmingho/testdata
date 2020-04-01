#!/usr/bin/env python3
import struct

fname = 't'
with open(fname, 'wb') as fp:
    fp.write(struct.pack('B', 0))
    fp.write(struct.pack('B', 10))
    fp.write(struct.pack('B', 50))
    fp.write(struct.pack('B', 100))
    fp.write(struct.pack('B', 150))
    fp.write(struct.pack('B', 200))
    fp.write(struct.pack('B', 250))
    fp.write(struct.pack('B', 255))

with open(fname, 'rb') as fp:
    while True:
        data = fp.read(1)
        if not data:
            break
        print(struct.unpack('B', data)[0])
