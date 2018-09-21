Writeup 3 - OSINT II, OpSec and RE
======

Name: Anand Raghu
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Anand Raghu

## Assignment 3 Writeup

### Part 1 (100 pts)
Hi Fred, I am glad you decided to converse with me regarding potential fixes for your security issues revolving about your company server. There are a few main points I'd like to talk to you about, namely your weak password, your exposed ports, and your negligence regarding personal identifying information online.

For your password, I would like to stress how insecure `pokemon` is as a choice. By simply running a brute force attack using a list of leaked passwords, I was able to gain access to your server in about 25 mins, which is almost nothing if you think about how much faster newer and evolved forms of password cracking really are. To that point, I would also like you to note that the password was found in an ancient word list, so people have been using your password for quite a number of years before you, which only adds to the insecurity because it is a very common password/term. Furthermore with some research, I have found that it is bad practice to simply have all lowercase or all alphabet characters, you should really mix and match a variety of letters, numbers, and symbols. Checking your password on `LastPass` and `How Secure Is My Password` yields a number of warnings, with the latter saying that the password can be cracked instantly, and the former asking you to add more characters and a variety of them as well. If you wanted to be extra thorough, you could even generate a random password through a multitude of ways (dice, random character generators online, etc) and use those instead. Just make sure you don't store those passwords in plaintext!


My next big issue with your server is the exposed port you left available for me to find and use to gain access to your system. By leaving port 1337 open, you risk leaving yourself vulnerable to attack at any time, because if I was able to get in, then others will most defintely find their way too. It looks like you are trying to leave yourself a way to connect to the shell running on your server so you can do various maintainence tasks or whatnot, so I would reccommend that you simply use SSH instead. It is exactly the solution you need for your situation, and in fact is widely used, so it has stood strong against the test of time and continues to work today. If you insist on having a unique port with that service running, might I suggest having a whitelist of IPs that can connect, or at least implement a retry feature that will ban IPs that try to log on for an absurd amount of time.. I would also like to note that a lot of security issues are compounding, so if even if you did transition towards Secure Shell and closed down port vulnerabilities, if you still have a weak password, that would present an easier target for an attacker. 

Lastly, I would like to talk about the information you put online. A surprising amount of the "hacking" we do is simply gleaning information from social media or other sources you might not be aware of. For example, I was able to easily guess your username for the shell connection simply based on your email, and I was able to steal flight data based on an instagram post you made. For these, you might consider basic privacy steps, like making your social media private and available to only friends, or hiding your email behind a simple "Contact Us" form on your website. You should also hide who provides the technical infrastructure for your system, because then it would be much harder to guess possible usernames/passwords based on personality. Registering your domain under an LLC versus your name or similar things can be a big hinderance towards people with malicious intent.


Thank you for your time, and wishing you best in future endeavors,

-h4ck3r m@n
