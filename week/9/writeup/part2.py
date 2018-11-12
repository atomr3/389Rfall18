#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

reg = re.compile("(\w+) hash of (\w+)")
# too easy
while True:
	data = s.recv(1024)
	valid = reg.search(data)
	if not valid:
		break
	vals = valid.groups()
	s.send(getattr(hashlib,vals[0])(vals[1]).hexdigest() + "\n")
	pass
print(data)

# close the connection

s.close()
