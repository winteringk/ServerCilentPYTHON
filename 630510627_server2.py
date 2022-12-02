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

client_socket, addr = ss.accept()      
print("Got a connection from %s" % str(addr))

while True:
   num = client_socket.recv(1024).decode('ascii')

   if num in ('q', 'Q'):
      break
   if num.isnumeric():
   # number only
      print('from connected user:', num)
      x = int(num)**2
      print('sending:', x)
      client_socket.send(str(x).encode('ascii'))
   else:
      print('from connected user:', num)
      result = 'cannot calculate' + num
      print(result)
      client_socket.send(result.encode('ascii'))
      
   #msg = 'Thank you for connecting'+ "\r\n"
   #client_socket.send(msg.encode('ascii'))
client_socket.close()