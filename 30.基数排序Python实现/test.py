# -*- coding: utf-8 -*-
# 十进制的基数排序
curcle_num = 1

def radixSort(a):
	
	global curcle_num
	temp = [0]*len(a)

	while max(a)/curcle_num >0:	
		count_num = [0]*10
		for i in range(len(a)):
			count_num[a[i]/curcle_num%10]+=1

		print ("count_num00:",count_num)

		for i in range(1,len(count_num)):
			count_num[i] += count_num[i-1]

		print ("count_num:",count_num)

		for i in range(len(a)-1,-1,-1):
			count_num[a[i]/curcle_num%10] = count_num[a[i]/curcle_num%10] -1
			temp[count_num[a[i]/curcle_num%10]] = a[i]

		for i in range(len(a)):
			a[i] = temp[i]
		curcle_num *=10 
		print ("temp:",temp)


if __name__ =="__main__":
	a = [170, 45, 75, 90, 2, 24, 802, 66]
	radixSort(a)