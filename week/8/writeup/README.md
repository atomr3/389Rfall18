Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Anand Raghu
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Anand Raghu

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. They used it on the cornerstoneairlines website - 142.93.118.186 and facebook

2. Names: laz0rh4x, c0uchpot4doz

3. laz0rh4x - `IP: 104.248.224.85` - `Location: North Bergen, NJ`
	c0uchpot4doz - `IP: 206.189.113.189` - `Location: London, UK`

4. Port 2749

5. They mentioned plans for something tomoorrow at 1500, which I'm assuming is 3pm

6. They sent a link to a file on google drive `https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view`

7. They expect to see each other tomorrow.

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1. Generated on Oct. 25 2018 @ 12:40:07 am

2. authored by `laz0rh4x`

3. Says it has `9` sections, really has `11`

4. 
SECTION
Type : ascii
Length : 51
Call this number to get your flag: (422) 537 - 7946


SECTION
Type : array of words
Length : 15
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]


SECTION
Type : coordinates
(38.99161, -77.02754)


SECTION
Type : reference section
1


SECTION
Type : ascii
Length : 60
The imfamous security pr0s at CMSC389R will never find this!


SECTION
Type : ascii
Length : 991
The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand.In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}

SECTION
Type : coordinates
(38.9910941, -76.9328019)


SECTION
Type : png


SECTION
Type : ascii
Length : 22
AF(saSAdf1AD)Snz**asd1


SECTION
Type : ascii
Length : 45
Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9



SECTION
Type : dwords
Number dwords : 6
[4, 8, 15, 16, 23, 42]

5. Flags : `CMSC389R-{c0rn3rst0ne_airlin3s_to_the_m00n}` from png, `CMSC389-{h1dd3n-s3ct10n-1n-fil3}` decoded from base64 from the dwords, and `CMSC389R-{PlaIN_dIfF_FLAG}` from the steg paragraph description.
