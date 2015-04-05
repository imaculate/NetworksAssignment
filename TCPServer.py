#import socket module
#python3 was used for this assignment hence the code has been adjusted accordingly.
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket

serverPort = 8970

serverSocket.bind(("",serverPort))
serverSocket.listen(1)

while True:
#Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)#get http header file.
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()
        #Send one HTTP header line into socket
        #Fill in start
        header = "HTTP/1.0 200 OK\r\nContent-Type: text/html\n\n"
        connectionSocket.send(header.encode())
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        error = "404 Not Found"
        connectionSocket.send(error.encode())
        connectionSocket.close()
    
        