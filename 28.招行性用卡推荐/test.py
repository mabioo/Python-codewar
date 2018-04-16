
# 现在信用卡开展营销活动，持有我行信用卡客户推荐新户办卡，开卡成功后可获得积分奖励。
# 规定每个客户最多可推荐两个新户且一个新户只能被推荐一次。但允许链接效应，
# 即若客户A推荐了新户B，新户B推荐新户C，则客户C同时属于A和B的推荐列表。
# 简单起见，只考虑以一个老客户A作起点推荐的情况。编程计算推荐新户数不小于n的客户列表。


# if __name__ == "__main__":
# 	base_num = str(raw_input())
# 	print "base:",base_num
# 	person = int(base_num[0])
# 	spc_num = int(base_num[2])

# 	list_info = []
# 	for i in range(person):
# 		list_info.append(str(raw_input()))
# 	#list_info = ["A B C","C F *","B D E","D G *","E H I"]

# 	result_list = []
# 	for i in range(person):
# 		list_info[i] = list_info[i].replace("*","")
# 		list_info[i] = list_info[i].replace(" ","")
# 		if len(set(list(list_info[i]))) >spc_num:
# 			#print list_info[i]
# 			result_list.append(list_info[i][0])

# 	result_list = set(result_list)	
# 	print " ".join(result_list)

while True:
    try:
        mn = raw_input()
        mn = mn.split()
        m = int(mn[0])
        n = int(mn[1])
        res = []
        for i in range(m):
            res.append(raw_input().split())
        if n == 0:
            result = []
            for i in range(m):
                for j in range(3):
                    if res[i][j] != '*':
                        result.append(res[i][j])
            result = list(set(result))
            if len(result) == 0:
                print(None)
                break
            else:
                print(' '.join(result))
                break
        l1 = []
        for i in range(m):
            l1.append(res[i][0])
        print "res:",res
        print "l1:",l1
        def f(x):
            if x not in l1:
                return 0
            else:
                index = l1.index(x)
                if res[index][2] == '*':
                    return 1 + f(res[index][1])
                else:
                    return 2 + f(res[index][1]) + f(res[index][2])
        result = []
        for i in range(m):
            if f(l1[i]) >= n:
                result.append(l1[i])
        if len(result) == 0:
            print(None)
        else:
            print(' '.join(result))
    except:
        break
