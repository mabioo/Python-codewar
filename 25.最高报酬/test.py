if __name__ =="__main__":
	tem = str(raw_input()).split(" ")
	num_jobs = int(tem[0])
	num_person = int(tem[1])

	dict_jobs = {}
	for i in range(num_jobs):
		tem1 = str(raw_input()).split(" ")
		dict_jobs[int(tem1[0])] = int(tem1[1])

	abli_list = list(set(dict_jobs))
	abli_person = str(raw_input()).split(" ")

	result = []
	for i in range(num_person):
		for j in range(len(abli_list)):
			if int(abli_person[i]) >= abli_list[j] and int(abli_person[i]) < abli_list[j+1]:
				result.append(dict_jobs[abli_list[j]])

	for i in range(len(result)):
		print result[i]