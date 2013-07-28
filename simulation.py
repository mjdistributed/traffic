""" the workhorse of the project """

from traffic_map import *
from agent import *
from visualize import *

def square_setup():
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

	origin.set_cross_road_segments(list([left_road_seg, top_road_seg]))
	top_right.set_cross_road_segments(list([top_road_seg, right_road_seg]))
	bottom_right.set_cross_road_segments(list([right_road_seg, bottom_road_seg]))
	bottom_left.set_cross_road_segments(list([bottom_road_seg, left_road_seg]))

	#origin.cross_road_segments = set([top_road_seg, left_road_seg])
	#top_right.cross_road_segments = set([top_road_seg, right_road_seg])
	#bottom_right.cross_road_segments = set([right_road_seg, bottom_road_seg])
	#bottom_left.cross_road_segments = set([bottom_road_seg, left_road_seg])

	road_segments = set([top_road_seg, right_road_seg, left_road_seg, bottom_road_seg])
	intersections = set([origin, top_right, bottom_right, bottom_left])

	dir1 = LeftDirection(square_road)
	dir2 = RightDirection(square_road)
	car1 = Car(top_road_seg, 2, 10, dir1)
	car2 = Car(bottom_road_seg, 2, 10, dir2)
	cars = set([car1, car2])
	return TrafficGraph(road_set, road_segments, intersections, cars)

def cross_road_setup():
	top = Intersection(0, 5)
	bottom = Intersection(10, 5)
	left = Intersection(5, 0)
	right = Intersection(5, 10)
	middle = Intersection(5, 5)

	vert_road = Road("vertical road", set([top, middle, bottom]))
	horiz_road = Road("horizontal road", set([left, middle, right]))
	road_set = set([vert_road, horiz_road])
	top_road_seg = Road_Segment(vert_road, [top, middle])
	bottom_road_seg = Road_Segment(vert_road, [middle, bottom])
	left_road_seg = Road_Segment(horiz_road, [left, middle])
	right_road_seg = Road_Segment(horiz_road, [middle, right])

	top.set_cross_road_segments(list([top_road_seg]))
	bottom.set_cross_road_segments(list([bottom_road_seg]))
	left.set_cross_road_segments(list([left_road_seg]))
	right.set_cross_road_segments(list([right_road_seg]))
	middle.set_cross_road_segments(list([top_road_seg, bottom_road_seg, left_road_seg, right_road_seg]))

	road_segments = set([top_road_seg, bottom_road_seg, left_road_seg, right_road_seg])
	intersections = set([top, middle, bottom, left, right])

	dir1 = RightDirection(vert_road)
	dir2 = RightDirection(horiz_road)
	car1 = Car(top_road_seg, 0, 10, dir1)
	car2 = Car(left_road_seg, 0, 10, dir2)
	car3 = Car(left_road_seg, 0, 10, dir2)

	cars = set([car1, car2, car3])
	return TrafficGraph(road_set, road_segments, intersections, cars)

def more_complex_graph_setup():
	vert_road_len = horiz_road_len = 40
	intersection_density = 3
	intersections = list()
	for i in range(vert_road_len + 1):
		for j in range(horiz_road_len + 1):
			if(i%intersection_density == 0 and j%intersection_density == 0):
				intersections.append(Intersection(i, j))

	roads = list()
	for i in range(vert_road_len + 1):
		if(i % intersection_density == 0):
			roads.append(Road("vert road " + str(i), filter(lambda inter: inter.y == i, intersections)))
	for i in range(horiz_road_len + 1):
		if(i % intersection_density == 0):
			roads.append(Road("horiz road " + str(i), filter(lambda inter: inter.x == i, intersections)))

	road_segments = set()
	#add horiz road segments
	for road_index in range(len(roads)/2, len(roads)):
		curr_intersections = roads[road_index].intersections
		for i in range(1, len(curr_intersections)):
			new_road_seg = Road_Segment(roads[road_index], list([curr_intersections[i-1], curr_intersections[i]]))
			road_segments.add(new_road_seg)
	#add vertical road segments
	for road_index in range(len(roads)/2):
		curr_intersections = roads[road_index].intersections
		for i in range(1, len(curr_intersections)):
			new_road_seg = Road_Segment(roads[road_index], list([curr_intersections[i-1], curr_intersections[i]]))
			road_segments.add(new_road_seg)
	
	#set cross-road segments on each intersection
	for intersection in intersections:
		cross_road_segments = list()
		for road_seg in road_segments:
			if intersection in road_seg.endpoints:
				cross_road_segments.append(road_seg)
		intersection.set_cross_road_segments(cross_road_segments)

	cars = set()
	trafficGraph = TrafficGraph(roads, road_segments, set(intersections), set())
	add_new_cars(trafficGraph, 0)
	add_new_cars(trafficGraph, 3)
	return trafficGraph


def painFunction(waiting_time):
	return pow(waiting_time, 2)


def score(trafficGraph):
	look_ahead = trafficGraph.copy()
	for car in look_ahead.cars:
		car.act()
	penalty = 0
	for car in look_ahead.cars:
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
		for cross_road_segment in traffic_light.cross_road_segments:
			prev_state = copy(traffic_light.light)
			traffic_light.switch_signal(cross_road_segment)
			curr_score = score(trafficGraph)
			if(curr_score < min_score):
				min_score = curr_score
			else:
				traffic_light.light = prev_state
	trafficGraph


def solve_it():
	vis = Visualize()
	print("solving...")
	trafficGraph = more_complex_graph_setup()
	num_states = 20#45#60*24
	num_iters = 1
	states = list()
	for i in range(num_states):
		newState = trafficGraph.copy()
		newState.cars = trafficGraph.cars #we want cars to persist across states
		states.append(newState)
	file = open("test_file.txt", "w")
	for i in range(num_iters):
 		for currGraph in states:
			perturb(currGraph)
			vis.draw(currGraph, 40, file)
			for car in trafficGraph.cars:
				car.act()
		for car in trafficGraph.cars:
			car.reset_position()
	file.close()
	return states


def add_new_cars(trafficGraph, starting_pos):
	"""Adds a new car at the start of each road segment in the graph"""
	road_segments = list(trafficGraph.road_segments)
	#set directions & cars for vertical roads
	for road_seg in filter(lambda seg: seg.endpoints[0].x == starting_pos and seg.endpoints[0].y == seg.endpoints[1].y, road_segments):
		direction = RightDirection(road_seg.road)
		trafficGraph.cars.add(Car(road_seg, starting_pos, 10, direction))
	#set directions & cars for horiz roads
	for road_seg in filter(lambda seg: seg.endpoints[0].y == starting_pos and seg.endpoints[0].x == seg.endpoints[1].x, road_segments):
		direction = RightDirection(road_seg.road)
		trafficGraph.cars.add(Car(road_seg, starting_pos, 10, direction))


print("running...")
import traffic_map
import agent
import visualize
reload(traffic_map)
reload(agent)
reload(visualize)
#x = simulate("nothing")

solve_it()