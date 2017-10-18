class Room(object):
	"""docstring for Room"""
	def __init__(self, _name):
		self.name = _name
		self.clients = {}


	def new_client(client):
		self.clients[client.address] = client

	def on_client_recv(client, test):
		print "Connection recieved...", " room name: ", self.name
		