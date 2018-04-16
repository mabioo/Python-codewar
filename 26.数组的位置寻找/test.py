def super_street_fighter_selection(fighters, position, moves):
	current_x = position[0]
	current_y = position[1]
	solution = []
	# print (moves)
	# print (fighters)
	# print (position)
	if len(moves) == 0:
		return []

	for i in range(len(moves)):
		if moves[i] == "left":
			current_y -=1
			if current_y<0:
				current_y = len(fighters[0])-1
			while fighters[current_x][current_y] == "":
				current_y -=1
				if current_y<0:
					current_y = len(fighters[0])-1
			solution.append(fighters[current_x][current_y])

		if moves[i] == "right":
			current_y +=1
			if current_y>(len(fighters[0])-1):
				current_y = 0
			while fighters[current_x][current_y] == "":
				current_y +=1
				if current_y>(len(fighters[0])-1):
					current_y = 0
			solution.append(fighters[current_x][current_y])

		if moves[i] == "up":
			current_x -=1
			if current_x <0:
				current_x = 0
			if fighters[current_x][current_y] == "":
				current_x +=1
				if current_x >(len(fighters)-1):
					current_x = len(fighters)-1
			solution.append(fighters[current_x][current_y])

		if moves[i] == "down":
			current_x +=1
			if current_x >(len(fighters)-1):
				current_x = len(fighters)-1
			if fighters[current_x][current_y] == "":
				current_x -=1
				if current_x <0:
					current_x = 0
			print fighters[current_x][current_y]
			solution.append(fighters[current_x][current_y])

	return solution

if __name__ == "__main__":
	fighters = [['Blanka', 'Guile', '', 'Chun Li'], 
	['M.Bison', 'Zangief', 'Dhalsim', 'Sagat'], 
	['', 'Ryu', 'E.Honda', 'Cammy'], 
	['Deejay', 'Cammy', '', 'T.Hawk'], 
	['Balrog', 'Ken', 'Chun Li', ''], 
	['Vega', '', 'Fei Long', 'Balrog']]
	moves =  ['left', 'left', 'up', 'left', 'up', 'left', 'down', 'down', 'right', 'up', 'right', 'down', 'left', 'right', 'up', 'up', 'up', 'left', 'up', 'up', 'left', 'down', 'left']
	#moves = ["down"]
	position = (0,1)


	print (super_street_fighter_selection(fighters,position,moves))


# ['Blanka', 'Chun Li', 'Balrog', 'Fei Long', 'Chun Li', 'Ken', 'Ken', 'Ken', 
# 'Chun Li', 'Chun Li', 'Balrog', 'Vega', 'Balrog', 'Vega', 'Balrog', 'Deejay', 
# 'Deejay', 'T.Hawk', 'Cammy', 'Sagat', 'Dhalsim', 'E.Honda', 'Ryu'] 
# should equal 
# ['Blanka', 'Chun Li', 'Chun Li', 'Guile', 'Guile', 'Blanka', 'M.Bison', 'M.Bison', 
# 'Zangief', 'Guile', 'Chun Li', 'Sagat', 'Dhalsim', 'Sagat', 'Chun Li', 'Chun Li', 
# 'Chun Li', 'Guile', 'Guile', 'Guile', 'Blanka', 'M.Bison', 'Sagat']