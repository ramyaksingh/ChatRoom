import socket

HOST, PORT = '', 8000

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = {}
listen_socket.bind((HOST, PORT))
listen_socket.listen(10)
print('Serving HTTP on port %s ...' % PORT)

while True:

    client_connection, client_address = listen_socket.accept()
    clients[client_address] = client_connection
    print('New client in room ...' + str(client_address[0]) + ' ' + str(client_address[1]))

    while(True):


        request = clients[client_address].recv(1024)

        print(request.decode())

        clients[client_address].send("Type something else: ".encode())

clients[client_address].close()
