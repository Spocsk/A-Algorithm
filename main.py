import fonctions
import time
import os
from fonctions import *

time_start = time.perf_counter()

history_move = []

terrain = generate_maze()
start, end = start_end(terrain)

while(True):

	cellule = scan(start,terrain)
	#print(cellule)
	backup = backup_scan(cellule)

	somme, h_dist, s_min, h_min = check_distance(start, cellule, end)
	new_cellule = shortest_distance(cellule, somme, h_dist, s_min, h_min)

	if new_cellule in history_move:
		cellule.remove(new_cellule)
		somme, h_dist, s_min, h_min = check_distance(start, cellule, end)
		new_cellule = shortest_distance(cellule, somme, h_dist, s_min, h_min)


	terrain[new_cellule[1]][new_cellule[0]] = "◊"
	history_move.append(new_cellule)
	start = new_cellule

	time.sleep(0.6)
	clear = lambda: os.system('cls') #on Windows System
	clear()
	if new_cellule == end:
		break

	print_maze(terrain)
print_maze(terrain)

time_end = time.perf_counter() #calculate the time of execution
print("execution time : {} secondes".format(round(time_end - time_start,6)))
print("Algorithme solve the problem in {} moves".format(len(history_move)))
input("Press enter to exit !")

