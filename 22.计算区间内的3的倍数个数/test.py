def func(a):
	if a%3 == 0 or a%3 == 1:
		return (a/3)*2
	else :
		return ((a/3)*2 + 1)

if __name__ == "__main__":
    i= str(raw_input(""))
    a = i.split(" ")
    result = 0
    c = func(int(a[0]))
    d = func(int(a[1]))
    print ("func0:%s func1:%s",(c,d))
    result = d -c
    if((int(a[0])-1)%3 !=0):
    	result += 1
    print (result)