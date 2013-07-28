class Visualize:
 
	def draw(self, traffic_graph, square_size, open_file = None):
		mat = [[] for i in range(square_size+1)]
		for i in range(square_size + 1):
			for j in range(square_size + 1):
				mat[i].append("") 
		for car in traffic_graph.cars:
			row = 0
			column = 0
			if(get_orientation(car.road_segment) == "vertical"):
				if(car.road_segment.endpoints[0].x > car.road_segment.endpoints[1].x):
					row = car.road_segment.endpoints[0].x - car.road_position
				else:
					row = car.road_segment.endpoints[0].x + car.road_position
				column = car.road_segment.endpoints[0].y
			else:
				if(car.road_segment.endpoints[0].y > car.road_segment.endpoints[1].y):
					column = car.road_segment.endpoints[0].y - car.road_position
				else:
					column = car.road_segment.endpoints[0].y + car.road_position
				row = car.road_segment.endpoints[0].x
			mat[row][column] += "0"
		for intersection in traffic_graph.intersections:
			row = intersection.x
			column = intersection.y
			if "green" in intersection.light:
				index = intersection.light.index("green")
				green_segment = intersection.cross_road_segments[index]
				if(get_orientation(green_segment) == "horizontal"):
					mat[row][column] += "--"
				else:
					mat[row][column] += "|"
			else:
				mat[row][column] += "X"

		#print
		for ray in mat:
			output_row = format_row(ray)
			print(output_row)
			if(open_file != None):
				open_file.write(output_row + "\n")
		if(open_file != None):
			open_file.write("-" * (square_size * 4) + "\n")

def get_orientation(road_segment):
	endpoints = road_segment.endpoints
	if(endpoints[0].x - endpoints[1].x == 0):
		return "horizontal"
	if(endpoints[0].y - endpoints[1].y == 0):
		return "vertical"
	else:
		raise Exception("error: road segment not horizontal or vertical")

def format_row(mat_row):
	output_str = ""
	for val in mat_row:
		if(val == ""):
			output_str += "  "
		else:
			if len(val) == 1:
				output_str += val + " "
			else:
				output_str += val
	return output_str