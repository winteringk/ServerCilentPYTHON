import socket, select, errno, sys
from datetime import datetime

# Limit length name
HEADER = 10

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = socket.gethostname()
PORT = 9999

client_socket.connect((HOST, PORT))

client_socket.setblocking(False)


my_username = input("Username: ")
un = my_username.encode('ascii')

un_header = f"{len(un):<{HEADER}}".encode('ascii')

client_socket.send(un_header + un)


while True:

    message = input(f'{my_username} >> ')

    if message:

        # Encode message to bytes, prepare header and convert to bytes, like for username above, then send
        ms = message.encode()
        ms_header = f"{len(message):<{HEADER}}".encode('ascii')
        client_socket.send(ms_header + ms)

    try:
        
        while True:
            un_header = client_socket.recv(HEADER)

            if not len(un_header):
                print('Connection closed by the server')
                sys.exit()

            username_length = int(un_header.decode('ascii').strip())

            username = client_socket.recv(username_length).decode('ascii')

            message_header = client_socket.recv(HEADER)
            message_length = int(message_header.decode('ascii').strip())
            message = client_socket.recv(message_length).decode('ascii')
            
            time_now = datetime.today()
            now = time_now.strftime('%H:%M')
            
            print(f'{username} {now} \n >> {message}')

    except Exception as e:
        print('Reading error: {}'.format(str(e)))
        sys.exit()