""" the workhorse of the project """


from traffic_map import *
from agent import *

def simulate(nothing):
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
	left_road_seg = Road_Segment(square_road, [origin, bottom_left])
	bottom_road_seg = Road_Segment(square_road, [bottom_left, bottom_right])
	car1 = Car(top_road_seg, 10)
	#car1.start()
	#act
	print("acting...")
	#while(True):
	car1.act()
	car1.act()
	car1.act()


def painFunction(watitingTime):
	return pow(waitingTime, 2)


def score(trafficGraph):
	val penalty = 0
	for car in trafficGraph.cars:
		penalty += painFunction(car.watitingTime)
	return penalty

def score_solution(trafficGraph_sequence):
	val score = 0
	for trafficGraph in trafficGraph_secuence:
		score += score(trafficGraph)

def perturb(trafficGraph):
	val min_score = 100000000
	val optimal_state = null
	for traffic_light in trafficGraph.intersections
		traffic_light.switchSignal
		val curr_score = score(trafficGraph)
		if(curr_score < min_sscore)
			min_score = curr_score
		else
			traffic_light.switchSignal
	trafficGraph


def solve_it():
	val trafficGraph = setup()
	val num_states = 60*24
	val num_iters = 100
	val states = List()
	for i in range(num_states):
		states += trafficGraph.copy
	for i in num_iters:
		for currGraph in states:
			perturb(currGraph)
	return states


print("running...")
import traffic_map
import agent
reload(traffic_map)
reload(agent)
x = simulate("nothing")