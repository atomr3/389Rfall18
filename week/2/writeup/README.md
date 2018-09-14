Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Anand Raghu
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Anand Raghu

## Assignment 2 writeup

### Part 1 (45 pts)

1. Fred Krueger

2. Twitter: kruegster1990 - created in August 2018
   From Silver Spring, MD. Born in 1990
   Instagram: kruegster1990 
   Reddit: kruegster1990 - created on August 13th, 2018
   Personal website: http://www.cornerstoneairlines.co/
   Tutanota email:  kruegster@tutanota.com
   Startaid account: http://www.startaid.com/user/kruegster1990/
   No idea what this is: https://zaralarsson115206071.wordpress.com/2018/08/12/kruegster1990/
   Additional details: He seems to enjoy pokemon, from his instagram photos, and travels between Baltimore and San Francisco.

   Explanation: I started with a simple Google search for the username, which quickly pointed me in the direction of his Twitter account, which was a real goldmine. From his bio, I got to his personal webpage for his business, as well as his location, year of birth, and his creation date. After that, I used multiple user-name checking websites from inteltechniques to find his reddit, instagram, and Startaid account. I cross referenced the results from each to make sure I was not getting false positives, which in some cases I thought I did, as the websites seemed to have the userID but gave me a 404 instead. The email address was gleaned from his webpage contact info, and the zaralarsson wordpress site is still a mystery to me.


3. The webserver IP address is '142.93.118.186', and I found this by doing a reverse domain lookup, which yielded a bunch of information such as this.

4. I looked at the robots.txt for the website to find any forbidden pages, and I found the secret page, which after looking at the source, yielded a flag of 'CMSC389R-{fly_th3_sk1es_w1th_u5}'.

5. When you click on the 'Admin' page, you get an undisguised IP as a URL, which is '142.93.117.193'. In addition, doing a search with ipinfo.io, you can find the routing IP for DigitalOcean which is 142.93.112.0/20.


6. In terms of associated servers, I only found 2 nameservers relative to the website.

7. The operating system running is Ubuntu Linux, and I discovered this from checking out the http headers for the site.

8. Another flag I found in the source was 'CMSC389R-{h1dden_fl4g_in_s0urce}'

### Part 2 (55 pts)

For this part, I was slightly overwhelmed at first, but realized it was not that bad. I struggled to find the right port to use at first, because I had used `nmap` on the wrong IP. After scanning all ports on the IP address gleaned from the 'Admin' page, several open ones popped up, and the only strange one was `1337`. After testing it out with `nc`, I wrote a simple python script which just iterated through the rockyou.txt wordlist and tried every password until login did not fail. To find the correct username for the login, I just tried the email username found on the website, because I figured it would not be kruegster1990. Once I found the password, which was `pokemon`, I got access to the shell, and from there, I navigated to the folder of flight records, and grabbed the one that matched the photo on the instagram account. 

The flag is `CMSC389R-{c0rn3rstone-air-27670}`.






