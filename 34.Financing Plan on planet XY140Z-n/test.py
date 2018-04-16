# -*- coding:utf-8 -*-


def sumALL(start,end):
	i = start
	sum_part = 0 
	while i<=end:
		sum_part += i
		i = i+1
	return sum_part

def finance(n):
	result = 0
	i = 0
	while i<=n: 
		result =result +sumALL(i,n)
		i += 2
		n +=1
	return result

if __name__ =="__main__":
	print (finance(6))




