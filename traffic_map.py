from sets import Set
from math import *
from copy import copy

class Intersection:
	"""An intersection on a trafic map"""

	def __init__(self, x, y, cross_road_segments = None):
		self.x = x
		self.y = y
		if(cross_road_segments == None):
			self.cross_road_segments = list()
		else:
			self.cross_road_segments = cross_road_segments
		self.light = list()
		for i in range(len(self.cross_road_segments)):
			self.light.append("red")

	def set_cross_road_segments(self, cross_road_segments):
		self.cross_road_segments = cross_road_segments
		self.light = list()
		for i in range(len(self.cross_road_segments)):
			self.light.append("red")

	def getDistance(self, other):
		return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))

	def switch_signal(self, road_segment):
		index = self.cross_road_segments.index(road_segment)
		if(index < 0 or index >= len(self.cross_road_segments)):
			raise Exception("error: road segment doesn't got through intersection")
		print(self.light)
		if(self.light[index] == "red"):
			self.light[index] = "green"
			for i in range(len(self.cross_road_segments)):
				if(i != index):
					self.light[i] = "red"
		else:
			self.light[index] = "red"

	def get_light(self, road_segment):
		return self.light[self.cross_road_segments.index(road_segment)]

	def next_segment(self, from_segment, which_way):
		if(which_way == "straight"):
			for road_seg in self.cross_road_segments:
				if(road_seg.road == from_segment.road and road_seg != from_segment):
					return road_seg
			raise Exception("couldn't find cross road")
		else:
			raise Exception("unsupported!!")

	def copy(self):
		inter_copy = Intersection(copy(self.x), copy(self.y), copy(self.cross_road_segments))
		inter_copy.light = copy(self.light)
		return inter_copy

	def __str__(self):
		return "Intersection at (" + str(self.x) + ", " + str(self.y) + ")"

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

	def __init__(self, road, endpoints):
		self.road = road
		self.endpoints = endpoints
		self.length = endpoints[0].getDistance(endpoints[1])
		self.positions = range(0, int(ceil(self.length)))

	def set_endpoints(endpoints):
		self.endpoints = endpoints

	def get_endpoints(self):
		return self.endpoints

	def get_road(self):
		return self.road

	def set_road(self, road):
		self.road = road

	def get_next_position(self, curr_position, direction):
		"""RightDirection goes in positive dir, LeftDirection goes in negative dir"""
		if direction.dir() == "right":
			if(curr_position < self.length):
				return curr_position + 1
			else:
				return curr_position
		else:
			if(curr_position > 0):
				return curr_position - 1
			else:
				return 0

	def get_intersection(self, curr_position):
		if(curr_position != self.length and curr_position != 0):
			raise Exception("error in get_intersection: curr_position is not at an intersection")
		if(curr_position == 0):
			return self.endpoints[0]
		else:
			return self.endpoints[1]

	def is_at_intersection(self, curr_position):
		if(curr_position == self.length or curr_position == 0):
			return True
		else:
			return False

	def __str__(self):
		return "road segment of road '" + str(self.road) + "' with endpoints " + str(self.endpoints[0]) + " and " + str(self.endpoints[1])

class RightDirection:
	"""either right or left"""

	def __init__(self, road):
		self.road = road

	def __str__(self):
		return "RightDirection on " + str(self.road)

	def dir(self):
		return "right"


class LeftDirection:
	def __init__(self, road):
		self.road = road

	def __str__(self):
		return "LeftDirection on " + str(self.road)

	def dir(self):
		return "left"


class TrafficGraph:
	def __init__(self, roads, road_segments, intersections, cars):
		self.roads = roads
		self.road_segments = road_segments,
		self.intersections = intersections
		self.cars = cars



	def copy(self):
		roads_copy = copy(self.roads)
		road_segments_copy = copy(self.road_segments)
		intersections_copy = self.intersections.copy()
		cars_copy = set([])
		for car in self.cars:
			cars_copy.add(car.copy())
		return TrafficGraph(roads_copy, road_segments_copy, intersections_copy, cars_copy)




"""global road1 = Road()
global road2 = Road()
global road3 = Road()
global roads = Set([road1, road2, road3])"""