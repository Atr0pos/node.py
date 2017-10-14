import socket
import thread
import client
import room

clients = {}
rooms = {}

def on_new_client(data,addr):
	clients[addr] = data


def on_existing_client():
	pass

def on_create_room_request(room_name):

	pass



hostname = "127.0.0.1"
port = 5005

print "Starting server..."

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

print "Server started...."

sock.bind((hostname, port))

print "Waiting for clients..."


while 1:
	data, addr = sock.recvfrom(1024)
	if addr in clients:

	clients[addr] = Id
	print "Connection recieved...", addr

	thread.start_new_thread()

	print data


sock.close()


#clientsocket.close()