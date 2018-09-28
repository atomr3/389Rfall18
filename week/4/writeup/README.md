Writeup 3 - Pentesting I
======

Name: Anand Raghu
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Anand Raghu

## Assignment 4 Writeup

### Part 1 (45 pts)

The right flag is as follows: `CMSC389R-{p1ng_as_a_$erv1c3}`. After the hint about command injection, I was fairly confident that a basic approach to finding the flag was all that was required and that the input was not sanitized to prevent chaining multiple commands together. After `nc`ing to cornerstoneairlines.co I simply put a semi-colon in the input section for the IP address to ping, and then adjoined exploratory commands after to find the flag in the home dir. Specifically, I used `;cat /home/flag.txt`. I was paranoid that it was a little too easy, and the wording of the question in particular "the right flag" threw me off a bit, so to be doubly sure, I searched for all `.txt` files using `find . -type f -name "*.txt"`, of which I only found the one that contained the flag. To find the script, I wanted to dump the entire file system onto my personal computer, which would have made it easier for me to go through everything, but ended up running myself into the ground. I tried the `scp` command for file transfer, the tool `transfer.sh`, and even recursively printing all directerories and readable files and writing a ruby script to organize the output. I quickly realized that this was wasting my time, and I ended up just reusing the `find` command from earlier and searching for all shell scripts like so: `find . -type f -name "*.sh"`. This listed a few scripts, and the first one, `./opt/container_startup.sh` was what Fred used to check the uptime. From just looking at the script, it is clear that Fred was not sanitizing the input. A few suggestions I have would be to either escape all potentially malevolent characters, blacklist certain characters from the input such as ';' and '&', get the script to treat all the input as the data by surrounding it with quotes or some kind of Prepared-Statement-esq strategy, or restrict the input string to an IP address format.

### Part 2 (55 pts)

The stub.py file included in this section is basically a limited shell that grants you access to the cornerstoneairlines.co server. At first, you have an interface that lets you either drop into an extended shell, pull a file, display a help menu, or quit the shell, and malformed commands simply display the usage menu again (Color coded!). On entering the extended shell, you can navigate around the filesystem using `cd`, and you can execute regular commands like `cat` or `ls`. What is happening is that the program is locally keeping track of your working directory in the attack server, and everytime you execute a new command in the shell, it prepends a `;` char, and `cd <working-directory>;` to the command. This is now sent via the socket as one input string to the IP address prompt, where due to the principles of command injection, the string is evaluated as a chain of commands, first getting you into the right directory, then executing the next arbritary command. I did have some issues with newlines, as I forgot to strip the return of previous commands, which led to the shell not actually executing future commands after the initial one. In addition, I had to decode my return string, as I was getting an error revolving around the concat of byte+string. There is a small easter egg if you do `cat flag.txt` and the right flag is returned.