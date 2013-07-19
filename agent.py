import random
from copy import copy
from traffic_map import *


class Car:
	"""simulates a car moving through the map"""

	def __init__(self, road_segment, road_position = None, maxSpeed = None, direction = None):
		self.speed = 1
		self.waiting_time = 0
		self.road_segment = road_segment
		if(direction is not None):
			self.direction = direction
		else:
			self.direction = random.choice(road_segment.road.directions)
			print("direction: " + str(self.direction))
		if(maxSpeed is not None):
			self.maxSpeed = maxSpeed
		if(road_position is not None):
			self.road_position = road_position
		else:
			random.choice(self.road_segment.positions)
		self.start_position = copy(self.road_position)
		self.start_direction = copy(self.direction)
		self.start_road_segment = (self.road_segment)
		print("initialized car w/ direction " + str(self.direction))

	def act(self):
		for i in range(0, self.speed):
			new_position = self.road_segment.get_next_position(self.road_position, self.direction)
			if(new_position == self.road_position):
				print("at light")
				if(self.road_segment.is_at_intersection(new_position)):
					curr_intersection = self.road_segment.get_intersection(self.road_position)
					#go through the intersection if green
					if(curr_intersection.light == "green"):
						print("green!!!!")
						self.waiting_time = 0
						#turn or go straight
						#which_action = Random.choice(set[0,1,2])
						which_action = 0 #for now, always go straight
						#0 -> go straight
						if(which_action == 0):
							self.road_segment = curr_intersection.next_segment(self.road_segment, "straight")
							ends = self.road_segment.endpoints
							print("new road segment w/ endpoints: (" + str(ends[0].x) + ", " + str(ends[0].y) + ") and (" + str(ends[1].x) + ", " + str(ends[1].y) + ")" )
							if self.direction.dir() == "right":
								new_position = 0
							else:
								new_position = int(self.road_segment.length)
						print("new road position: " + str(new_position))
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

	def will_be_waiting(self):
		new_position = self.road_segment.get_next_position(self.road_position, self.direction)
		if(new_position == self.road_position):
			if(self.road_segment.is_at_intersection(new_position)):
				curr_intersection = self.road_segment.get_intersection(self.road_position)
				#go through the intersection if green
				if(curr_intersection.light == "green"):
					return 0
		return self.waiting_time

	def copy(self):
		return Car(self.road_segment, self.road_position, self.maxSpeed, self.direction)