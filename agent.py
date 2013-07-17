import random
from copy import copy


class Car:
	"""simulates a car moving through the map"""

	def __init__(self, road_segment = None, maxSpeed = None, direction = None):
		self.speed = 1
		self.waiting_time = 0
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
		self.start_position = copy(self.road_position)
		self.start_direction = copy(self.direction)
		self.start_road_segment = (self.road_segment)

	def act(self):
		for i in range(0, self.speed):
			new_position = self.road_segment.get_next_position(self.road_position, self.direction)
			if(new_position == self.road_position):
				if(self.road_segment.is_at_intersection(new_position)):
					curr_intersection = self.road_segment.get_intersection(self.road_position)
					#go through the intersection if green
					if(curr_intersection.light == "green"):
						self.waiting_time = 0
						#turn or go straight
						#which_action = Random.choice(set[0,1,2])
						which_action = 0 #for now, always go straight
						#0 -> go straight
						if(which_action == 0):
							self.road_segment = curr_intersection.next_segment(self.road_segment, "straight")
							if(isinstance(self.direction, RightDirection)):
								self.road_position = 0
							else:
								self.road_position = self.road_segment.length
						#1 -> turn right
						#if(which_action == 1):

						#2 -> turn left
						#if(which_action == 2):

					else:
						print("car waiting")
						self.waiting_time += 1
			self.road_position = new_position

	def reset_position(self):
		self.road_position = self.start_position
		self.direction = self.start_direction
		self.road_segment = self.start_road_segment