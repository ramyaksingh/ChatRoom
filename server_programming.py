import socket
from threading import *

class AsyncWrite(Thread):

    def __init__(self, serverToClientSocket, clientAddress):
        Thread.__init__(self)
        self.serverToClientSocket = serverToClientSocket
        self.clientAddress = clientAddress
        self.start()

    def run(self):
        self.serverToClientSocket.send("Enter your name: ".encode())
        name = self.serverToClientSocket.recv(1024).decode()
        print("New client in room. Say hello to " + name)

        while True:
            self.serverToClientSocket.send("Write something: ".encode())

            str = self.serverToClientSocket.recv(1024).decode()
            if(str == 'exit'):
                self.serverToClientSocket.close()
                break


            print(name + str)



def Main():
    HOST, PORT = '', 8888

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(10)
    print('Serving HTTP on port %s ...' % PORT)

    while True:

        client_connection, client_address = listen_socket.accept()
        #print('New client in room ...' + str(client_address[0]) + ' ' + str(client_address[1]))
        AsyncWrite(client_connection, client_address)

if(__name__ == '__main__'):
    Main()
