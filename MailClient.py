from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "myuct.ac.za"
serverPort = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver,serverPort))
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != "220":
    print("220 reply not received from server.")
# Send HELO command and print server response.
heloCommand = "HELO Alice\r\n"
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != "250":
    print('250 reply not received from server.')
#sendMailCommand
sendMailCommand = "MAIL FROM: <alice@196.47.234.247>"
clientSocket.send(sendMailCommand)
recv2 = clientSocket.recv(1024)
print(recv2)
if recv2[:3] != "250":
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcpttoCommand = "RCPT TO: <culey.resto@gmail.com>"
clientSocket.send(rcpttoCommand)
recv3 = clientSocket.recv(1024)
print(recv3)
if recv3[:3] != "250":
    print('250 reply not received from server.')
    
    
# Send DATA command and print server response.
clientSocket.send("DATA")
recv4 = clientSocket.recv(1024)
print(recv4)
if recv4[:3] != "354":
    print('354 reply not received from server.')
    
    
# Send message data.

clientSocket.send(msg)
clientSocket.send(endmsg)

# Message ends with a single period.
recv5 = clientSocket.recv(1024)
print(recv5)
if recv5[:3] != "250":
    print('250 reply not received from server.')
    
    
# Send QUIT command and get server response.
clientSocket.send("QUIT")
recv6 = clientSocket.recv(1024)
print(recv6)
if recv6[:3] != "221":
    print('221 reply not received from server.')