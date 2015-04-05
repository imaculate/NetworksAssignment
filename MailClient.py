from socket import *
import ssl
import getpass
import base64
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.gmail.com"

serverPort = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver,serverPort))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != "220":
    print("220 reply not received from server.")
# Send HELO command and print server response.
heloCommand = "EHLO google.com\r\n"
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != "250":
    print('250 reply not received from server.')
    
command = "STARTTLS\r\n"
clientSocket.send(command.encode())
recvdiscard = clientSocket.recv(1024).decode()
print(recvdiscard)
clientSocketSSL = ssl.wrap_socket(clientSocket)



heloCommand = "EHLO gmail.com\r\n"
clientSocketSSL.send(heloCommand.encode())
recv1 = clientSocketSSL.recv(1024).decode()
print(recv1)
if recv1[:3] != "250":
    print('250 reply not received from server.')
    
   
# Authentication required
Username = input("Insert Username: ")
Password = getpass.getpass("Password: ")

UserPass=base64.b64encode(("\x00" + Username + "\x00" + Password).encode('utf-8')).decode()

UserPass=UserPass.strip("\n")
print(UserPass)

#Userpass = "AUTH PLAIN " + UserPass + "\r\n"


clientSocketSSL.send("AUTH PLAIN\r\n".encode())
recv2 = clientSocketSSL.recv(1024).decode()
print(recv2)
if recv2[:3] != "334":
    print('334 reply not received from server.')
    
print("sent stuff!")
clientSocketSSL.send((UserPass + "\r\n").encode())
recv2 = clientSocketSSL.recv(1024).decode()
print(recv2)
    
    
#sendMailCommand
sendMailCommand = "MAIL FROM: <culey.resto@gmail.com>\r\n"
clientSocketSSL.send(sendMailCommand.encode())
print("sent mail from command")
recv2 = clientSocketSSL.recv(1024).decode()

print(recv2)
if recv2[:3] != "250":
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcpttoCommand = "RCPT TO: <mshima001@myuct.ac.za>\r\n"
clientSocketSSL.send(rcpttoCommand.encode())
recv3 = clientSocketSSL.recv(1024).decode()
print(recv3)
if recv3[:3] != "250":
    print('250 reply not received from server.')
    
    
# Send DATA command and print server response.
data = "DATA\r\n"
clientSocketSSL.send(data.encode())
recv4 = clientSocketSSL.recv(1024).decode()
print(recv4)
if recv4[:3] != "354":
    print('354 reply not received from server.')
    
    
# Send message data.

clientSocketSSL.send(msg.encode())
clientSocketSSL.send(endmsg.encode())

# Message ends with a single period.
recv5 = clientSocketSSL.recv(1024).decode()
print(recv5)
if recv5[:3] != "250":
    print('250 reply not received from server.')
    
    
# Send QUIT command and get server response.
clientSocketSSL.send("QUIT\r\n".encode())
recv6 = clientSocketSSL.recv(1024).decode()
print(recv6)
if recv6[:3] != "221":
    print('221 reply not received from server.')