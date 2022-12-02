#!/usr/bin/python3           # This is client.py file

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
s.connect((host, port))            

while True:
    n_ = input()

    if n_ in ('q', 'Q'):
        s.send(n_.encode('ascii'))
        break
    s.send(n_.encode('ascii'))

    re_cli = s.recv(1024).decode('ascii')
    print('Received from server:', re_cli)

s.close()
# C:/Users/Dell/AppData/Local/Programs/Python/Python39/python.exe c:/Users/Dell/Desktop/sc/Cilent.py