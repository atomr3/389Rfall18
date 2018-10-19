Writeup 7 - Forensics I
======

Name: Anand Raghu
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Anand Raghu

## Assignment 7 writeup

### Part 1 (40 pts)

1. JPEG image

2. It was taken in Chicago, Illinois at the John Hancock Center.

3. It was taken 2018:08:22 11:33:24.801

4. iPhone 8 back camera 3.99mm f/1.8

5. 539.5 meters above sea level

6. I found `CMSC389R-{look_I_f0und_a_str1ng}` by using `strings` and piping the output to a file and simply searching for `CMSC`. Another flag was found via `binwalk` which revealed 3 files hidden within image. After opening the png file I found `CMSC389R-{abr@cadabra}` as an image.

### Part 2 (55 pts)

At first I started by simply running the binary, which gave me an output that said "Where is your flag?". I then ran `strings` on the binary, which gave me a lot of garbage strings in the output. I grep'd it for "CMSC" to see if there were any flags, but I should have known that it would not be that easy. However, in this garbage dump, I did see some interesting identifiers like `fopen` and `fclose` and `fwrite` which told me that this binary was creating and writing to a file somewhere, most likely not within an easily guessable directory for me. Also in this text dump was `challenge`, a few words about data and some stuff about arrays like `reverse_array` which I thought might be relevant at that time. I used `find` to search for recently modified files since the time that I ran the binary, and I made it traverse through all subdirectories from root level. I got a bunch of garbage files, but one that caught my eye was `.stego` in /tmp. I then copied it over into my working dir in order to play with it. I ran `binwalk` on it, and it told me that there was a JPEG hidden inside after 1 byte. I removed the first null byte and copied it into a new file called `testfile`, and it was recognized as a JPEG, which after opening was a picture of some kind of dinosaur (I don't know dinosaurs well lol). I was lucky enough to try `steghide` on my first go at this puzzle, and using the documentation on their website, saw that I could extract data from an image. I then was prompted for a password which threw me off a little. I tried a few passwords that were keywords relating to the class, then my roommate walked by and asked why I was looking at a stegosaurus. I then learned that was the name of the dinosaur, after which I immediately used that as the password since it sounded so similar with the "steg-". Using the password extracted the flag to my directory, which contained `CMSC389R-{dropping_files_is_fun}`.
