if __name__ == "__main__":
	count_num = int(raw_input())
	rever_info = str(raw_input())
	dirs = ["N","E","S","W"]
	current_dirs = 0
	for i in range(count_num):
		if rever_info[i] == "L":
			current_dirs -=1
		else :
			current_dirs +=1
		if current_dirs < 0:
			current_dirs =3
		if current_dirs > 3:
			current_dirs =0
	print dirs[current_dirs]
