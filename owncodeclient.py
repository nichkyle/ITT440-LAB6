import socket
import signal
import sys

ClientSocket = socket.socket()
host = '192.168.56.119'
port = 8888

print('\n\t\t********************Connected********************')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode("utf-8"))
while True:
    Input = input('\nEnter your operation and number:  ')

    if Input == 'quit':
        break
    else:
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode("utf-8"))

ClientSocket.close()
