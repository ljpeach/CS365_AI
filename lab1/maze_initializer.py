def maze_initializer(file):
	text = open(file, "r")
	file_contents = text.readlines()
	text.close()
	maze_array = list()
	prize_position = list()
	for i in file_contents:
		maze_array.append(list(i.strip()))
	for i in maze_array:
		for j in i:
			print(j, end = "")
		print()
	for i in range(len(maze_array)):
		for j in range(len(maze_array[i])):
			if maze_array[i][j] == "P":
				mouse_position = (i,j)
			if maze_array[i][j] == ".":
				prize_position.append((i,j))
	return (mouse_position, prize_position, maze_array)

result = maze_initializer("multiprize-medium.txt")
print(result)
