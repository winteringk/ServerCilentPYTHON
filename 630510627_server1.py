#!/usr/bin/python3           # This is server.py file

import socket                                         

# create a socket object
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999                                           

# bind to the port
ss.bind((host, port))                                  

# queue up to 5 requests
ss.listen(5)                                           

while True:
   # establish a connection
   client_socket, addr = ss.accept()      

   print("Got a connection from %s" % str(addr))
    
   msg = 'Thank you for connecting'+ "\r\n"
   client_socket.send(msg.encode('ascii'))
   client_socket.close()