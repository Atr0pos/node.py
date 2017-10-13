import socket
import thread

def on_new_client(clientsocket,addr):
    while True:
	    msg = clientsocket.recv(1024) 
	    #do some checks and if msg == someWeirdSignal: break:
	    #print addr, ' >> ', msg
	    msg = raw_input('SERVER >> ') 
	    #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
	    #clientsocket.send(msg) 


hostname = "127.0.0.1"
port = 5005

print "Starting server..."

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # UDP

print "Server started...."

sock.bind((hostname, port))

print "Waiting for clients..."

sock.listen(5)





while 1:
	c, addr = sock.accept()
	print "Connection recieved...", addr
	thread.start_new_thread(on_new_client,(c,addr))

socket.close()


#clientsocket.close()