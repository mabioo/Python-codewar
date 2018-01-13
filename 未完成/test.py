# -*- coding:utf-8 -*-

def permutations(string):

#this is for calculate the factorial of n
	def factorial(n):
		s= 1 
		for i in range(2,n+1):
			s = s*i
		return s

	#this is for combination C(m,n)
	def combination(m,n):
		return factorial(n)/(factorial(n-m)*factorial(m))

	#this is for rank A(m,n)
	def ranks(m,n):
		return factorial(n)/factorial(n-m)
	

	#输出当前循环需要遍历的个数
	def sumcombintation(lists,nums):
		count = 1
		for i in lists:
			count = count*combination(i,nums)
			nums= nums -i
		return int(count)

	def changeTarget(text,elements,indexs):
		a = list(text)	
		if indexs>len(text)-1:
			indexs = indexs -len(text)
		#print ("indexs",indexs)
		for i in range(len(a)):
			if a[i] =="0":				
				if indexs ==0:
					a[i] = elements
					break
				indexs = indexs -1

		return "".join(a)


	#def addPara(elements,times):

	numberOfchar = len(string)   #不同字符的个数
	sumOfchar = [string.count(i) for i in string] #字符串的个数列表
	targetList = ["0"*len(string)]*sumcombintation(sumOfchar,len(string))
	#print ("factorial",factorial(3))
	#print ("combination:",combination(2,4))
	#print ("lenof lsit:",type(sumcombintation(sumOfchar,len(string))))

	print ("numberOfchar:",numberOfchar)
	print ("sumOfchar:",sumOfchar)
	print ("targetList",targetList)
	#print ("test:",changeTarget("000","a",0))
	for i in string:
		duplicateChar = ranks(numberOfchar-2,numberOfchar-1)
		print ("duplicateChar",duplicateChar)
		cucletemp = duplicateChar
		#对每个单词进行添加
		indexs = 0
		for j in range(len(targetList)):
			if (cucletemp==0):
				indexs = indexs +1  
				cucletemp = duplicateChar
			targetList[j] = changeTarget(targetList[j],i,indexs)
			print (targetList[j])
			cucletemp = cucletemp -1
		numberOfchar  = numberOfchar -1

	print ("targetList",targetList)


if __name__ == "__main__":
	permutations("abc")