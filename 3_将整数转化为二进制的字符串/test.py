def add_binary(a,b):
	sum = a+b
	tarstr =[]

	while (sum != 0):
		tarstr.append(sum%2)
		sum = sum/2
	tarstr.reverse()
	target = ''.join(map(str,tarstr))
	return target
	#return tarstr.reverse().toString()


if __name__ =="__main__":
	print add_binary(0,9)