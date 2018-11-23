Writeup 10 - Crypto II
=====

Name: Anand Raghu
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Anand Raghu

## Assignment 10 Writeup

### Part 1 (70 Pts)
For this part, I automated socket connections to the server, after `nc`ing in, because I quickly realized that manually interacting would be kind of painful, due to the amount of copy and pasting within the terminal.
For step 1, I simply sent my message to be signed via the socket, and grabbed the hash from the response. I used this to initialize the state of the md5 we have, and then updated it with my malicious message 'InfoSci'. Then I printed out the new false hash which represents the supposed payload.

For step 2, we know that the secret size is between 6-16, so we iterate through that range. Size of 64 minus 8 minus 1 for the preceding 1 byte, which in total is 55. Then we subtract the message length and the secret size, which yields the padding. With this, we can send the payload which is message + padding + malicious joined together. In order to recieve the full data, I put in a sleep because I was not recieving the entirity of the message. I then just simply checked whether there was the beginning of a flag contained within the message text, and printed out the correct message. 


Flag `CMSC389R-{i_still_put_the_M_between_the_DV}`


### Part 2 (30 Pts)
There's basically 3 commands that you really need for this part, one to generate a key - `gpg --gen-key`, one to import the secret key given - `gpg --import filename`, and then one to encrypt the final message - `gpg --output filename.private --encrypt --recipient president@csec.umiacs.umd.edu filename.`

