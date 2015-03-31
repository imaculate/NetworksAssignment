from socket import *
import getpass
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
heloCommand = "HELO Alice\r\n"
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != "250":
    print('250 reply not received from server.')
   
    # Authentication required
Username = input("Insert Username: ")
Password = getpass.getpass("Password: ")
UserPass=("\x00" + Username + "\x00" + Password)
UserPass=UserPass.strip("\n")
#print("AUTH PLAIN " + UserPass)
Userpass = "AUTH PLAIN " + UserPass + "\r\n"

clientSocket.send(UserPass.encode())
print("sent stuff!")
recv2 = clientSocket.recv(1024).decode()
print(recv2)
    
#sendMailCommand
sendMailCommand = "MAIL FROM: <alice@196.47.234.247>"
clientSocket.send(sendMailCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != "250":
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcpttoCommand = "RCPT TO: <culey.resto@gmail.com>"
clientSocket.send(rcpttoCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != "250":
    print('250 reply not received from server.')
    
    
# Send DATA command and print server response.
data = "DATA"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != "354":
    print('354 reply not received from server.')
    
    
# Send message data.

clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())

# Message ends with a single period.
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != "250":
    print('250 reply not received from server.')
    
    
# Send QUIT command and get server response.
clientSocket.send("QUIT")
recv6 = clientSocket.recv(1024)
print(recv6)
if recv6[:3] != "221":
    print('221 reply not received from server.')