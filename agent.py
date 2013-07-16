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
			new_position = self.road_segment.get_next_position(self.road_position, self.direction)
			if(new_position == self.road_position):
				if(self.is_at_intersection()):
					#go through the intersection if green
					if(intersection.light == "green"):
						#turn or go straight
						#which_action = Random.choice(set[0,1,2])
						which_action = 0 #for now, always go straight
						#0 -> go straight
						if(which_action == 0):

						#1 -> turn right
						if(which_action == 1):

						#2 -> turn left
						if(which_action == 2):

					else:
						self.waiting_time ++
			self.road_position = new_position
