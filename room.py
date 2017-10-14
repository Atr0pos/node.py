class Room(object):
	"""docstring for Room"""
	def __init__(self, _name):
		self.name = _name
		self.clients = [client()]