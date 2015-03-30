#this code was written using python 3. hence has been modified 
from socket import *
from datetime import datetime
from time import time
serverName = "196.47.234.247"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

for i in range(10):
    a = datetime.now()
    message = "Ping "+str(i+1)+" "+ str(a)
    
   
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    clientSocket.settimeout(1)
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        b = datetime.now()
        c = b-a
        print("Round trip time:", c.microseconds/1000000)
        msg = modifiedMessage.decode()
        print(msg)
    except timeout:
        print("Request timed out!")
clientSocket.close()