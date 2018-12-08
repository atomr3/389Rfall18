Writeup 10 - Crypto II
=====

Name: Anand Raghu
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Anand Raghu

## Assignment 10 Writeup

### Part 1 (70 Pts)
After playing around with the site for a bit, I was a little confused on how exactly I would perform this SQL attack, as there was no clear user input that would allow me to send text which would result in a malformed command for the query. However, after a bit I noticed that the URL changed reflecting which item I had clicked on, in a pattern like `item?id={#itemNumber}` where itemNumber is the ID of the object, which is used to fetch the text to display on the following page. After changing the ID number, it became clear that this was the method in order to enforce a tautalogy which would result in all the objects being dropped, which would hopefully reveal a flag. I used to Postman to GET the page with my attemped SQL injections, as I could easily parse the entire HTML for text similar to the flag and be notified immediately whether there was a match. The command that ended up working was basically very similar to the wikipidea page on OR extension attacks which was `' OR '1'='1`. This yielded the slightly misspelled flag `CMSC38R-{y0U-are_the_5ql_n1nja}`

### Part 2 (30 Pts)

**1.** This one was super easy from my 330 knowledge last semester, I just put the script tags with `alert(0);` in between, which worked.

**2.** This one was trickier. Script tags were blacklisted, but others were not. I knew the img tag had JS attributes, so I put one in with `onload="alert(0);"`  which worked. I later clicked the hints and saw that onerror would have worked as well.

**3.** I had a lot of trouble with this one, so I looked at the source code. It turned out to be pretty similar to our Part 1 at least with the URL, as they were combining the user input string with the `img` tag in order to load the proper image. I simply added the `.jpg'"` followed by another `"onerror="alert(0);/>""`

**4.** This one was actually fairly simple I thought. I assumed it would build off of the last challenge as the previous ones had done, and this one would also have string concatenation. I started putting random characters that would malform string concats like newlines and such, and when I put in a single quote the timer never started. After looking at the quote, I put `);alert(;`

**5.** This one was hard. I tried a bunch of tricks with the email form, and after looking at the source code realized that it was never really used, so my only real form of attack would be the browser bar again with the confirm query. After using all the hints, I read the IETF draft and figured I just needed to add `javascript:alert(0);` instead of confirm, which worked.

**6.** I had trouble with hosting my own JS file, was not sure what to do with this challenge :/


