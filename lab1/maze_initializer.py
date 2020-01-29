'''
takes a txt file as maze input, will add argparse later
'''

def maze_initializer(file):
	text = open(file, "r")
	file_contents = text.readlines()
	text.close()

	maze_array = list()
    # the 2D array used to represent the maze

	prize_position = list()
    # a list record the position of the prizes

	for i in file_contents:
		maze_array.append(list(i.strip()))
	# 2D array generated

    # code to print the maze for easier visualization
    #for i in maze_array:
	#	for j in i:
	#		print(j, end = "")
	#	print()

	for i in range(len(maze_array)):
    # iterate through the array to get the position of the mouse, append the prize position

        for j in range(len(maze_array[i])):
		    if maze_array[i][j] == "P":
			    mouse_position = (i,j)
		    if maze_array[i][j] == ".":
			    prize_position.append((i,j))

	return (mouse_position, prize_position, maze_array)
