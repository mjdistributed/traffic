class Visualize:
 
	def draw(self, traffic_graph, square_size):
		mat = [[] for i in range(square_size+1)]
		for i in range(square_size + 1):
			for j in range(square_size + 1):
				mat[i].append("") 
		for car in traffic_graph.cars:
			x_pos = 0
			y_pos = 0
			if(get_orientation(car.road_segment) == "vertical"):
				x_pos = car.road_segment.endpoints[0].x
				y_pos = car.road_segment.endpoints[0].y + car.road_position
			else:
				y_pos = car.road_segment.endpoints[0].y
				x_pos = car.road_segment.endpoints[0].x + car.road_position
			print("car pos: " + str(x_pos) + ", " + str(y_pos))
			mat[y_pos][x_pos] = "0"
		for intersection in traffic_graph.intersections:
			x_pos = intersection.x
			y_pos = intersection.y
			if(intersection.light == "green"):
				mat[y_pos][x_pos] = "G"
			else:
				mat[y_pos][x_pos] = "R"
		#print
		for ray in mat:
			print(ray)


def get_orientation(road_segment):
	endpoints = road_segment.endpoints
	if(endpoints[0].x - endpoints[1].x == 0):
		return "horizontal"
	if(endpoints[0].y - endpoints[1].y == 0):
		return "vertical"
	else:
		raise Exception("error: road segment not horizontal or vertical")
