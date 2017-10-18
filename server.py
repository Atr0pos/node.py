import socket
import thread
import client
import room
import json
import validator

clients = {}
rooms = {}




hostname = "127.0.0.1"

port = 5005

print "Starting server..."

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

print "Server started...."

sock.bind((hostname, port))

print "Waiting for clients..."

def on_new_client(data,addr):
	clients[addr] = client.Client(addr, data["username"])
	print "username: ", data["username"]

def on_existing_client(client, data):
	print client.username, " says ", data["message"]
	pass

while 1:

	data, addr = sock.recvfrom(1024)
	
	data = validator.handle_socket_data(data)
	
	
	#if the client exists
	if addr in clients:
		on_existing_client(clients[addr], data)
		#print "Connection recieved...", addr, " existing client: " , data 
		continue

	#client does not exist
	else:
		on_new_client(data, addr)
		#print "Connection recieved...", addr, " new client"
		continue
pass



sock.close()




#clientsocket.close()