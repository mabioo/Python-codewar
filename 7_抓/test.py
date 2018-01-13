# def find_outlier(int):
#     odds = [x for x in int if x%2!=0]
#     evens= [x for x in int if x%2==0]
#     return odds[0] if len(odds)<len(evens) else evens[0]

def find_outlier(integers):
    judge = sum([integers[i]%2 for i in range(3)])
    print (judge)
    for i in integers:
    	if (judge<=1):
    		if i%2 == 1:
    			return i
    	else:
    		if i%2 ==0:
    			return i

if __name__ =="__main__":
	print (find_outlier([2, 4, 6, 8, 10, 3]))



