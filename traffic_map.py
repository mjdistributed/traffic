from sets import Set
from math import *



class Intersection:
	"""An intersection on a trafic map"""

	def __init__(self):
		neighbors = Set()
		self.x = 0
		self.y = 0

	def __init__(self, x, y):
		neighbors = Set()
		self.x = x
		self.y = y

	def getDistance(self, other):
		return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))

class Path:
	"""2 Intersections & the distance between them"""
	def __init__(self, start, end):
		self.intersection1 = start
		self.intersection2 = end
		self.distance = getDistance(start, end)


class Road:
	"""A road on a traffic map"""


	def __init__(self, name, intersections):
		self.directions = (LeftDirection(self), RightDirection(self))
		self.name = name
		self.intersections = intersections

	def set_intersections(intersections):
		self.intersections = intersections

	def get_intersections():
		return self.intersections

	def __str__(self):
		return self.name

class Road_Segment:
	"""A road on a traffic map"""

	def __init__(self):
		self.intersections = Set()

	def __init__(self, endpoints):
		self.endpoints = endpoints

	def __init__(self, road, endpoints):
		self.road = road
		self.endpoints = endpoints
		self.length = endpoints[0].getDistance(endpoints[1])
		self.positions = range(0, int(ceil(self.length)))

	def set_endpoints(endpoints):
		self.endpoints = endpoints

	def get_endpoints(self):
		return self.intersections

	def get_road(self):
		return self.road

	def set_road(self, road):
		self.road = road

	def get_next_position(self, curr_position, direction):
		"""RightDirection goes in positive dir, LeftDirection goes in negative dir"""
		if isinstance(direction, RightDirection):
			print("moving right...")
			if(curr_position < self.length):
				return curr_position + 1
			else:
				return curr_position
		else:
			print("moving left...")
			if(curr_position > 0):
				return curr_position - 1
			else:
				return 0

class RightDirection:
	"""either right or left"""

	def __init__(self, road):
		self.road = road

	def __str__(self):
		return "RightDirection on " + str(self.road)


class LeftDirection:
	def __init__(self, road):
		self.road = road

	def __str__(self):
		return "LeftDirection on " + str(self.road)


class TrafficGraph:
	def __init__(self, roads, road_segments, intersections, cars):
		self.roads = roads
		slef.road_segments = road_segments,
		self.intersections = intersections
		self.cars = cars




"""global road1 = Road()
global road2 = Road()
global road3 = Road()
global roads = Set([road1, road2, road3])"""