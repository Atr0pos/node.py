import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

data = '{"username": "pbrady"}'

sock.sendto(data ,(UDP_IP,UDP_PORT))

while 1:
	msg = raw_input("Message: ")
	sock.sendto(msg, (UDP_IP, UDP_PORT))