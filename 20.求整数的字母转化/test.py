def factorial(n):
    S = 1
    while n>0:
        S=S*n
        n = n-1
    return S

def dec2FactString(nb):
    i = 1

    targetList = ""
    while (nb >= factorial(i)):
        i = i+1
    i = i-1
    print (i)
    while i>=0:
        j = 1
        while nb>=factorial(i)*j:
            j = j+1
        j =j-1
        nb = nb -factorial(i)*(j)
        i = i-1
        if j>35:
            j = j-35
        if(j >=10):
            t = chr(ord("A")+j-10)
        else:
            t = str(j)
        targetList= targetList+ t
    return targetList


def factString2Dec(string):
    j =0
    Sums = 0
    for i in range(len(string)-1,-1,-1):
        temp =string[i]
        if ord(temp)>=65:
            temp = ord(temp) - ord("A") +10
        Sums = Sums + factorial(j)*int(temp)
        j = j+1
    return Sums

#the best solutions:
Base36='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def factString2Decs(string):
  l,r=len(string)-1,0
  for i in range(0,l):
      r=(r+Base36.index(string[i]))*(l-i)
  return r

def dec2FactStrings(nb):
  l=['0']
  c,tmp=2, 0
  while(nb!=0):
      tmp=nb%c
      l.insert(0,Base36[tmp])
      nb=(nb-tmp)/c
      c+=1
  return ''.join(l)

if __name__ =="__main__":
    print (dec2FactString(23))
    #print (factorial(12))
    print (factString2Dec("3210"))
    #print (dec2FactString(9))
    print (factString2Decs("3210"))
