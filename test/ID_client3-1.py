#!/usr/bin/python3           # This is client.py file

import time, socket, sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = socket.gethostname()                           
port = 9999

s.connect((host, port))   

# Enter username
name = input('Enter username: ')
s.send(name.encode())

server_name = s.recv(1024).decode('ascii')

print(server_name, 'is online!')

# while True:
    
#     msg = s.recv(1024)                                     

# s.close()
# print (msg.decode('ascii'))