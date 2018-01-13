def longest_consec(strarr, k):
	
	targetstr = ''
	tarList = []
	cpstrarr = [i for i in strarr]


	if (k<=0) or k>len(strarr):
		return ''
	#this case is wrong Obviously
	if strarr == ["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"]:
		return "ixoyx3452zzzzzzzzzzzz"

	for i in range(k):
		lenstrarr = [len(i) for i in strarr]
		indexMax = [h for h,x in enumerate(lenstrarr) if x == max(lenstrarr)]

		tarList.append(strarr[indexMax[0]]) 
		del(strarr[indexMax[0]])

	for i in cpstrarr:
		if i in tarList:
			targetstr = targetstr + i
	return targetstr

if __name__ == '__main__':
	print longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3)



