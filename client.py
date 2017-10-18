import room

class Client(object):
	def __init__(self, adr, _username, _room="none"):
		self.username = _username
		self.address = adr
		self.room = room.Room(_room)