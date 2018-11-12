#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase
hashes = open("../hashes", 'r')
# makes it nice and easy
hashes = hashes.read().split("\n")

for word in wordlist:
	# need to clean this up otherwise won't work
	word = word.strip()
	for salt in salts:
		# what is naming convention in python?
		t_hash = hashlib.sha512(salt+word).hexdigest()
		if t_hash in hashes:
			print("Salt: %s\n" % salt)
			print("Password: %s\n" % word)
			pass

