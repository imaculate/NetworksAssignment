from socket import *
 

import base64
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.gmx.com"

serverPort = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver,serverPort))
recv = clientSocket.recv(1024)
print recv
if recv[:3] != "220":
    print("220 reply not received from server.")
# Send HELO command and print server response.
heloCommand = "EHLO gmx.com\r\n"
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != "250":
    print '250 reply not received from server.'
    

   
# Authentication required
Username= "uct.student@gmx.com"
Password = "UCTstudent123&&"


UserPass=base64.b64encode(("\x00" + Username + "\x00" + Password).encode('utf-8'))

UserPass=UserPass.strip("\n")
print UserPass

#Userpass = "AUTH PLAIN " + UserPass + "\r\n"


clientSocket.send("AUTH PLAIN\r\n")
recv2 = clientSocket.recv(1024)
print recv2 
if recv2[:3] != "334":
    print '334 reply not received from server.'
    
print "sent stuff!"
clientSocket.send((UserPass + "\r\n"))
recv2 = clientSocket.recv(1024)
print recv2
    
    
#sendMailCommand
sendMailCommand = "MAIL FROM: <uct.student@gmx.com>\r\n"
clientSocket.send(sendMailCommand)
print "sent mail from command"
recv2 = clientSocket.recv(1024)

print recv2
if recv2[:3] != "250":
    print '250 reply not received from server.'

# Send RCPT TO command and print server response.
rcpttoCommand = "RCPT TO: <imaculatemosha@yahoo.com>\r\n"
clientSocket.send(rcpttoCommand)
recv3 = clientSocket.recv(1024)
print recv3
if recv3[:3] != "250":
    print '250 reply not received from server.'
    
    
# Send DATA command and print server response.
data = "DATA\r\n"
clientSocket.send(data)
recv4 = clientSocket.recv(1024)
print recv4
if recv4[:3] != "354":
    print '354 reply not received from server.'
    
    
# Send message data.

clientSocket.send(msg)
clientSocket.send(endmsg)

# Message ends with a single period.
recv5 = clientSocket.recv(1024)
print recv5
if recv5[:3] != "250":
    print '250 reply not received from server.'
    
    
# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n")
recv6 = clientSocket.recv(1024)
print recv6
if recv6[:3] != "221":
    print '221 reply not received from server.'
