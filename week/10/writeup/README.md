Writeup 10 - Crypto II
=====

Name: Anand Raghu
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Anand Raghu

## Assignment 10 Writeup

### Part 1 (70 Pts)
For this part, I automated socket connections to the server, after `nc`ing in, because I quickly realized that manually interacting would be kind of painful, due to the amount of copy and pasting within the terminal.


Flag `CMSC389R-{i_still_put_the_M_between_the_DV}`


### Part 2 (30 Pts)
There's basically 3 commands that you really need for this part, one to generate a key - `gpg --gen-key`, one to import the secret key given - `gpg --import filename`, and then one to encrypt the final message - `gpg --output filename.private --encrypt --recipient p@csec.umiacs.umd.edu message.`

