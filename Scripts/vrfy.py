#!/usr/bin/python
#Script to probe a list of users through the command VRFY in a SMTP server.
##Author: Lezly Dialid Cerón Rodríguez

import socket
import sys

if len(sys.argv) != 3:
        print "Usage: vrfy.py <target ip> <list of users>"
        sys.exit(0)

# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
connect = s.connect((sys.argv[1],25))

# Receive the banner
banner = s.recv(1024)

print banner

#Read usernames from list
flist = open(sys.argv[2], 'r')
usernames = flist.readlines()

# VRFY usernames
for user in usernames:
        s.send('VRFY ' + user.strip() + '\r\n')
        result = s.recv(1024)
        print result

# Close the socket
s.close()