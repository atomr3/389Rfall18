Writeup 9 - Crypto I
=====

Name: Anand Raghu
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Anand Raghu

## Assignment 9 Writeup

### Part 1 (60 Pts)
`Solution:`
Salt: m
Password: jordan

Salt: u
Password: loveyou

Salt: k
Password: neptune

Salt: p
Password: pizza

For this part, it was pretty simple to bruteforce the salt and password combination. I simply went through the password list, then tried each one with the possible salts, and compared it to the hashes in the given file. If it was, then I printed it out, which yields the solution above.


### Part 2 (40 Pts)
`You win! CMSC389R-{H4sh-5l!ngInG-h@sH3r}` - Flag
For this challenge, I started by nc'ing to the address and manually playing around with the trivia game. I wasn't sure which representation of the hash it wanted (HEX vs hex) so I tried different ones until I determined it was the hexstring representation. I kept giving it the right answer but there was no end in sight. To automate this, I noted that the output text was the same with just the hash type and string to be hashed being different, so I just used regex to grab the match groups of the type and string, passed them through the hashlib, and sent it back to the server. I then uncovered the above flag.

