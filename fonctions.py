already_scan = []
previous_new_cellule = []


def generate_maze():

	terrain = []

	terrain.append(["■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■"])
	terrain.append(["■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," ","■"])
	terrain.append(["■","■"," ","■","■"," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■","■"," ","■","■"," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," ","■"," "," "," ","■"])
	terrain.append(["■"," "," "," "," "," "," "," ","■","■"," "," "," "," "," "," "," ","■","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■","■"," "," "," "," "," "," "," ","■","■"," "," "," "," "," "," "," "," "," "," "," ","■","■"," "," "," "," "," "," "," ","■","■"," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," "," "," "," ","■","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"])
	terrain.append(["■","■"," ","■","■"," ","■","■","■","■","■"," ","■","■"," ","■","■","■","■","■"," ","■","■"," ","■","■","■"," ","■","■"," ","■","■","■","■","■"," ","■","■"," ","■","■","■","■","■"," ","■","■","■"," ","■","■"," ","■","■","■","■","■"," ","■","■"," ","■","■","■","■","■"," ","■","■"," ","■","■","■"," ","■","■","■"," ","■","■"," ","■","■","■","■","■"," ","■","■"," ","■","■","■"," ","■","■"," ","■"," ","■","■","■"])
	terrain.append(["■"," "," ","■","■"," ","■"," "," "," "," "," ","■","■"," ","■"," "," "," "," "," ","■","■"," ","■"," "," "," ","■","■"," ","■"," "," "," "," "," ","■","■"," ","■"," "," "," "," "," ","■","■"," "," ","■","■"," ","■"," "," "," "," "," ","■","■"," ","■"," "," "," "," "," ","■","■"," ","■"," "," "," ","■"," "," "," ","■","■"," ","■"," "," "," "," "," ","■","■"," ","■"," "," "," ","■","■"," ","■"," ","■"," ","■"])
	terrain.append(["■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," "," ","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," "," ","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," "," ","■","■","■"," ","■"])
	terrain.append(["■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■","■","■"," ","■"])
	terrain.append(["■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," "," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," "," "," "," ","■"," ","■"," "," ","■"])
	terrain.append(["■"," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," "," "," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," ","■"])
	terrain.append(["■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," "," "," ","■"])
	terrain.append(["■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," "," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," "," "," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," "," "," ","■","■"," ","■"," ","■"," ","■"])
	terrain.append(["■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," ","■","■","■","■"," ","■"])
	terrain.append(["■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■","■","■"," ","■"])
	terrain.append(["■"," "," "," "," ","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," ","■"])
	terrain.append(["■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■","S"," ","■"," "," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," ","■"])
	terrain.append(["■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," "," "," ","■"])
	terrain.append(["■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■","■","■"," ","■"])
	terrain.append(["■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," "," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," "," "," "," ","■"," ","■"," "," ","■"])
	terrain.append(["■"," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," "," "," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," ","■"])
	terrain.append(["■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," "," "," ","■"])
	terrain.append(["■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," "," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," "," "," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," "," "," ","■","■"," ","■"," ","■"," ","■"])
	terrain.append(["■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," ","■","■","■","■"," ","■"])
	terrain.append(["■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■","■","■"," ","■"])
	terrain.append(["■"," "," "," "," ","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," ","■"])
	terrain.append(["■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," ","■"])
	terrain.append(["■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," "," "," ","■"])
	terrain.append(["■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," ","■"])
	terrain.append(["■","■"," ","■","■"," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■","■"," ","■","■"," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," ","■"," "," "," ","■"])
	terrain.append(["■"," "," "," "," "," "," "," ","■","■"," "," "," "," "," "," "," ","■","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■","■"," "," "," "," "," "," "," ","■","■"," "," "," "," "," "," "," "," "," "," "," ","■","■"," "," "," "," "," "," "," ","■","■"," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," "," "," "," ","■","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"])
	terrain.append(["■","■"," ","■","■"," ","■","■","■","■","■"," ","■","■"," ","■","■","■","■","■"," ","■","■"," ","■","■","■"," ","■","■"," ","■","■","■","■","■"," ","■","■"," ","■","■","■","■","■"," ","■","■","■"," ","■","■"," ","■","■","■","■","■"," ","■","■"," ","■","■","■","■","■"," ","■","■"," ","■","■","■"," ","■","■","■"," ","■","■"," ","■","■","■","■","■"," ","■","■"," ","■","■","■"," ","■","■"," ","■"," ","■","■","■"])
	terrain.append(["■"," "," ","■","■"," ","■"," "," "," "," "," ","■","■"," ","■"," "," "," "," "," ","■","■"," ","■"," "," "," ","■","■"," ","■"," "," "," "," "," ","■","■"," ","■"," "," "," "," "," ","■","■"," "," ","■","■"," ","■"," "," "," "," "," ","■","■"," ","■"," "," "," "," "," ","■","■"," ","■"," "," "," ","■"," "," "," ","■","■"," ","■"," "," "," "," "," ","■","■"," ","■"," "," "," ","■","■"," ","■"," ","■"," ","■"])
	terrain.append(["■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," "," ","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," "," ","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," "," ","■","■","■"," ","■"])
	terrain.append(["■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■","■","■"," ","■"])
	terrain.append(["■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," "," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," "," "," "," ","■"," ","■"," "," ","■"])
	terrain.append(["■"," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," "," "," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," ","■"])
	terrain.append(["■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," "," "," ","■"])
	terrain.append(["■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," "," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," "," "," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," "," "," ","■","■"," ","■"," ","■"," ","■"])
	terrain.append(["■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," ","■","■","■","■"," ","■"])
	terrain.append(["■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■","■","■"," ","■"])
	terrain.append(["■"," "," "," "," ","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," ","■"])
	terrain.append(["■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," ","■"])
	terrain.append(["■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," "," "," ","■"])
	terrain.append(["■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■","■","■"," ","■"])
	terrain.append(["■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," "," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," "," "," "," ","■"," ","■"," "," ","■"])
	terrain.append(["■"," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," "," "," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," ","■"])
	terrain.append(["■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," "," "," ","■"])
	terrain.append(["■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," "," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," "," "," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," "," "," ","■","■"," ","■"," ","■"," ","■"])
	terrain.append(["■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," ","■","■","■","■"," ","■"])
	terrain.append(["■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■","■","■"," ","■"])
	terrain.append(["■"," "," "," "," ","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," ","■"])
	terrain.append(["■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," ","■"])
	terrain.append(["■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," "," "," ","■"])
	terrain.append(["■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," "," ","■"," ","E","■"," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■","■"," "," ","■"," "," ","■"," ","■","■"," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," ","■"])
	terrain.append(["■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," "," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," "," "," ","■"," "," "," "," ","■"," "," "," ","■"," "," "," "," ","■"," "," "," "," "," "," ","■"," ","■"," "," ","■"])
	terrain.append(["■"," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," "," "," ","■"," "," "," ","■"," "," ","■"," ","■"," "," "," ","■"," "," ","■"," "," "," ","■"," "," ","■"," ","■"," ","■"])
	terrain.append(["■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■","■"," "," ","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■","■"," ","■","■"," "," "," ","■","■","■"," ","■","■"," "," "," ","■"," ","■","■"," "," "," "," "," ","■"])
	terrain.append(["■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," "," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," "," "," ","■","■"," "," ","■","■"," ","■"," ","■","■"," "," ","■","■"," ","■"," "," "," ","■","■"," ","■"," ","■"," ","■"])
	terrain.append(["■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," ","■","■"," "," ","■","■"," ","■","■","■","■"," ","■"])
	terrain.append(["■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," "," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■","■"," "," ","■"," ","■","■"," ","■","■"," "," ","■"," ","■","■"," "," "," ","■"," ","■","■","■","■"," ","■"])
	terrain.append(["■"," "," "," "," ","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," "," "," ","■"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","■"," "," "," "," ","■"])
	terrain.append(["■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■","■"])
	return terrain

def start_end(_maze):

	x = 0
	y = 0

	for bloc in _maze:
		for cellule in bloc:
			if cellule == "S":
				start = (x,y)
				#print("Start position = {}".format(start))

			if cellule == "E":
				end = (x,y)
				#print("End position = {}".format(end))
				
			if x == len(_maze[0])-1:
				y += 1
				x = 0
			else:
				x += 1

	return start, end


def scan(where_to_start,terrain):

	x_move = [-1,0,1]
	y_move = [0,1,-1]
	cellules = []
	cellule_found = []
	previous_cellule = []

	for w in y_move:
		for z in x_move:
			#check if x and y are in the terrain
			if (where_to_start[0] + x_move[z]) >= 0 and (where_to_start[0] + x_move[z]) <= len(terrain[0]) -1 and (where_to_start[1] + y_move[w]) >= 0 and (where_to_start[1] + y_move[w]) <= len(terrain)-1:
				explorer = (where_to_start[0] + x_move[z], where_to_start[1] + y_move[w]) #translate x to scan around the parent cellule
				if terrain[explorer[1]][explorer[0]] == "■":
					cellule_found.append("wall")
				else:
					cellule_found.append(explorer)
			else:
				cellule_found.append("err.") #else add in the list "error"
			#check if x and y are in the terrain
		if (where_to_start[0] + x_move[1]) >= 0 and (where_to_start[0] + x_move[1]) <= len(terrain[0])-1 and (where_to_start[1] + y_move[w]) >= 0 and (where_to_start[1] + y_move[w]) <= len(terrain)-1: 
			explorer = (where_to_start[0] + x_move[1], where_to_start[1] + y_move[w]) #translate y to scan around the parent cellule

			if terrain[explorer[1]][explorer[0]] == "■":
				cellule_found.append("wall")
			else:
				cellule_found.append(explorer)
		else:
			cellule_found.append("err.")

	for i in cellule_found:
		if i not in cellules:
			cellules.append(i)

	cellules.remove(where_to_start)

	if "err." in cellules:
		cellules.remove("err.")#remove wall and errors
	if "wall" in cellules:
		cellules.remove("wall")

	return cellules

def backup_scan(cellules_scan):

	for i in cellules_scan:
		if i not in already_scan:
			already_scan.append(i) #backup scan

	return already_scan

def check_distance(start_position, scanned, end_position):

	g_distance = []
	h_distance = []
	somme = []

	for p in range(0,len(scanned)):

		h = abs(end_position[0] - scanned[p][0]) + abs(end_position[1] - scanned[p][1]) #distance from cellule to end (Manhattan distance)
		h_distance.append(h)

		g = abs(start_position[0] - scanned[p][0]) + abs(start_position[1] - scanned[p][1]) #distance from cellule to start (Manhattan distance)
		g_distance.append(g)

		s = g+h
		somme.append(s)

	minimum_s = min(somme)
	minimum_h = min(h_distance)



	return somme, h_distance, minimum_s, minimum_h

def shortest_distance(from_scan, somme_res, h_distance,s_min,h_min):

	for elem in somme_res:
		if somme_res.count(elem) > 1:
			new_cellule = from_scan[h_distance.index(h_min)]
		else:
			new_cellule = from_scan[somme_res.index(s_min)]

	previous_new_cellule.append(new_cellule)

	return new_cellule


def print_maze(maze):

	for i in range(0,len(maze)): # print the maze
		print(*maze[i], sep=" ")