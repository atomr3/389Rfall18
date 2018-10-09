Writeup 5 - Binaries I
======

Name: Anand Raghu
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Anand Raghu

## Assignment 5 Writeup

I started this assignment by first reviewing the C files/methods we were given, so as to gain an idea of how to break them down into assembly, which we've done in CMSC216. After a quick glance, I realized the two programs were virtually the same, with the exception of what was being copied in memory. For the first, we were copying the same char, in this case 'z', repeatedly over the i length, and in the second, we were still copying over i length, except we were grabbing the ith byte from a dynamic string and copying it into the ith place. 

For the first, I basically I grabbed the parameter and placed it in 'rcx', and then looped through, while increasing 'rdi' in order to move forward. I ran into an issue regarding the exclamation mark not copying over, so I used 'sil' instead to access the lower byte. For the second function to implement, I used a slightly different approach, moving the memory from 'rsi' to 'dl', and then from 'dl' to 'rdi', which took care of any issues that were popping up. All in all, not a really bad project, it just took some getting used to regarding x86 syntax as well as memory size and management.
