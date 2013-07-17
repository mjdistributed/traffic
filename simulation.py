""" the workhorse of the project """

from traffic_map import *
from agent import *
from visualize import *

def setup():
	print("setting up ...")
	#setup
	origin = Intersection(0, 0)
	top_right = Intersection(0, 10)
	bottom_right = Intersection(10, 10)
	bottom_left = Intersection(10, 0)	

	road_set = set([origin, top_right, bottom_right, bottom_left])
	square_road = Road("square street", road_set)
	top_road_seg = Road_Segment(square_road, [origin, top_right])
	right_road_seg = Road_Segment(square_road, [top_right, bottom_right])
	left_road_seg = Road_Segment(square_road, [bottom_left, origin])
	bottom_road_seg = Road_Segment(square_road, [bottom_right, bottom_left])

	origin.cross_road_segments = set([top_road_seg, left_road_seg])
	top_right.cross_road_segments = set([top_road_seg, right_road_seg])
	print(top_right.cross_road_segments)
	bottom_right.cross_road_segments = set([right_road_seg, bottom_road_seg])
	bottom_left.cross_road_segments = set([bottom_road_seg, left_road_seg])

	road_segments = set([top_road_seg, right_road_seg, left_road_seg, bottom_road_seg])
	intersections = set([origin, top_right, bottom_right, bottom_left])

	dir = RightDirection(square_road)
	car1 = Car(top_road_seg, 8, 10, dir)
	cars = set([car1])
	return TrafficGraph(road_set, road_segments, intersections, cars)


def painFunction(waiting_time):
	return pow(waiting_time, 2)


def score(trafficGraph):
	penalty = 0
	for car in trafficGraph.cars:
		waiting_time = car.will_be_waiting()
		penalty += painFunction(waiting_time)
	return penalty

def score_solution(trafficGraph_sequence):
	score = 0
	for trafficGraph in trafficGraph_secuence:
		score += score(trafficGraph)

def perturb(trafficGraph):
	print("perturbing")
	min_score = score(trafficGraph)
	for traffic_light in trafficGraph.intersections:
		print("checking traffic light at (" + str(traffic_light.x) + ", " + str(traffic_light.y) + ")") 
		traffic_light.switch_signal()
		curr_score = score(trafficGraph)
		if(curr_score < min_score):
			min_score = curr_score
			print("optimal tlight is (" + str(traffic_light.x) + ", " + str(traffic_light.y) + ")") 
		else:
			traffic_light.switch_signal()
	trafficGraph


def solve_it():
	vis = Visualize()
	print("solving...")
	trafficGraph = setup()
	num_states = 16#60*24
	num_iters = 1
	states = list()
	for i in range(num_states):
		states.append(trafficGraph.copy())
	for i in range(num_iters):
		for currGraph in states:
			perturb(currGraph)
			for car in trafficGraph.cars:
				car.act()
			vis.draw(currGraph, 10)
		for car in trafficGraph.cars:
			car.reset_position()
	return states


print("running...")
import traffic_map
import agent
import visualize
reload(traffic_map)
reload(agent)
reload(visualize)
#x = simulate("nothing")

solve_it()