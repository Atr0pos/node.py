import json

def handle_socket_data(_data):
	try:
		d = json.loads(_data)
	except ValueError, e:
		print e

	return d