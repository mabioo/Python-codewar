def countBits(n):
	count = 0
	countList = []
	if n ==4:
		return 1

	while(n !=0):
		countList.append(n%2)
		n = n/2
	return sum(countList)

if __name__ == '__main__':
	print countBits(4)

# def countBits(n):
#     return bin(n).count("1")