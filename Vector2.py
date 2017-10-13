import math


class Vector2(object):

	def __init__(self, _x, _y):
		self.x = int(_x)
		self.y = int(_y)
		
	@classmethod
	def distance(cls, _v1, _v2):
		return  math.sqrt(	math.pow(	(_v1.x - v2.x), 2) + math.pow(	(_v1.y - _v2.y), 2)	)

