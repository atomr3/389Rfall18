#!/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")


with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

magic, version, time, author, num_sections = struct.unpack("<LLL8sL", data[0:24])
if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %d" % int(time))
print("AUTHOR: %s" % author)
print("NUM SECTIONS: %d" % num_sections)


print("-------  BODY  -------")
offset = 24
secs = 0
while offset < len(data):
    secs+= 1
    
    print("SECTION")
    stype, slen = struct.unpack("<LL", data[offset:offset+8])
    offset += 8
    if stype == 1:
        print("Type : png");
        f = open('output.png', 'w')
        f.write(str(data[offset:offset+slen]))
        offset += slen
    elif stype == 2:
    	# array of dwords
    	num = slen/8
        print("Type : dwords")
        print("Number dwords : %d" % (num))
        words = []
        for x in xrange(0,num):
        	words.append(struct.unpack("<Q", data[offset:offset+8])[0])
        	offset += 8
        	pass
        print(str(words))
    elif stype == 3:
        print("Type : utf8")
        print("Length : %d" % slen)
        print(data[offset:offset+slen].decode("utf-8"))
        offset += slen
    elif stype == 4:
        print("Type : array of doubles")
        num = slen/8
        print("Num doubles : %d" % num)
        d = []
        for x in xrange(0,num):
        	d.append(struct.unpack("<d", data[offset:offset+8]))
        	offset+=8
        	pass
        print(str(d))
    elif stype == 5:
        print("Type : array of words")
        num = slen/4
        print("Length : %d" % num)
        w = []
        for x in xrange(0,num):
        	w.append(struct.unpack("<L",data[offset:offset+4])[0])
        	offset+=4
        	pass
        print(str(w))
    elif stype == 6:
        print("Type : coordinates")
        print(struct.unpack("<dd", data[offset:offset+16]))
        offset += 16
    elif stype == 7:
        print("Type : reference section")
        print(struct.unpack("<I", data[offset:offset+4])[0])
        offset += 4
    elif stype == 9:
        print("Type : ascii")
        print("Length : %d" % slen)
        print(data[offset:offset+slen])
        offset += slen
    else:
        bork("No match with section type, you borked up fool")
    print("\n")