import random

class Car:
	"""simulates a car moving through the map"""

	def __init__(self, road_segment = None, maxSpeed = None, direction = None):
		self.speed = 1
		if(road_segment is not None):
			self.road_segment = road_segment
		if(direction is not None):
			self.direction = direction
		else:
			self.direction = random.choice(road_segment.road.directions)
			print("direction: " + str(self.direction))
		if(maxSpeed is not None):
			self.maxSpeed = maxSpeed
		self.road_position = random.choice(self.road_segment.positions)

	def act(self):
		print(self.road_position)
		for i in range(0, self.speed):
			self.road_position = self.road_segment.get_next_position(self.road_position, self.direction)
