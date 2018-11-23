#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import struct
import time

host = "142.93.118.186"
port = 1234

#####################################
### STEP 1: Calculate forged hash ###
#####################################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.recv(1024)

# go to sign some data
s.send('1\n')
s.recv(1024)

# make notary sign something and grab hash
s.send("Hello World\n")
data = s.recv(1024)
# grab last value of array which is hash
legit = data.split()[-1]     # a legit hash of secret + message goes here, obtained from signing a message
print("Real: " + legit) 

# i guess we need message after all, didn't pay too much attention to part 2 :/
# no newline char
message = "Hello World"


# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'InfoSci'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print("Fake: " + fake_hash)

# done


#############################
### STEP 2: Craft payload ###
#############################
# menu
s.recv(1024)

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits

# 64-8-1 = 55
# you would pad with 1 '1', then potentially 55 0's minus the secret and our own message
for x in xrange(6,16):
	l = len(message)
	l2 = struct.pack('<Q', ((x+l)*8))
	padding = '\x80' + ('\x00'*(55-l-x)) + l2
	payload = message + padding + malicious
	
	# test signature validity menu
	s.send("2\n")
	s.recv(1024)

	# send fake and payload
	s.send(fake_hash + "\n")
	s.recv(1024)
	s.send(payload + "\n")
	# too fast for the server :(, have to wait a bit for the response
	time.sleep(2)
	data = s.recv(2048)
	if 'CMSC389R' in data:
		print(data)
		break
		pass
	# print(data)


	pass

# payload is the message that corresponds to the hash in `fake_hash`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = fake_hash

# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!
