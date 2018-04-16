# -*- coding: utf-8 -*-

# 科室素拓进行游戏，游戏规则如下：随机抽取9个人作为游戏参与人员，分别编号1至9，
# 每轮要求k(k<=9且k>=0)个人自由组合使编号之和为n。输出满足规则的所有可能的组合。
# 要求组合内部编号升序输出，组合之间无顺序要求。

#s = input().split(" ")
s = "3 15".split(" ")
k = int(s[0])
n = int(s[1])
test = 1
answer = []
def sumOfNumber(sum,n,k):
    print (sum,n,k)
    if sum<=0 or n<=0 :
        return 
    if sum==n and k == 1:
        global test
        test = 2
        answer.reverse()
        print(n)
        for i in answer:
            print(i)
        #print()
        answer.reverse()
    answer.append(n)
    print answer
    print "&&&&&&&&&&&&&&&&&&&&&&&&&&&1"
    sumOfNumber(sum-n,n-1,k-1)
    print "&&&&&&&&&&&&&&&&&&&&&&&&&&&2"
    answer.remove(n)
    sumOfNumber(sum,n-1,k)
sumOfNumber(n,9,k)
if test == 1:
    print('None')

# Note: 2018.4.9:  看不懂这个题，关于嵌套比较难以理解
