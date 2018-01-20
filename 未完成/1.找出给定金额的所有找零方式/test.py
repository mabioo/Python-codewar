def temp(money,coins):
    coins.sort()
    coins.reverse()
    count_num = 0
    i = 0
    while i <len(coins):
        j = i
        count1 =1
        if tempMoney > coins[i]:
            tempMoney = money - coins[i]*count1
            count1 = count1 +1
        print ("$$$$$$$$$$$$$$$$$$$$$")
        while ( j<len(coins) ):
            print ("j:",j)
            print ("tempmonsy:",tempMoney)
            print ("con:",coins[j])
            if tempMoney >= coins[j]:
                tempMoney = tempMoney -coins[j]
            while (tempMoney >= coins[j]):
                if j != len(coins)-1 and (tempMoney-coins[j]<coins[j+1]) and (tempMoney-coins[j] !=0):
                    break
                else:   
                    tempMoney = tempMoney - coins[j]
            if tempMoney <= 2*coins[j]:
                j = j+1
            if tempMoney == 0:
                count_num = count_num +1
                tempMoney = money- coins[i]
            print ("count_num",count_num)
        i = i+1
    return count_num

if __name__ =="__main__":
    print(temp(30,[5,10,20]))