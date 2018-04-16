def convert(input, source, target):
    j = 0
    dec_value = 0
    #print ("intput:",input)
    #print ("souce:",source)
    #print ("target:",target)
    len_source = len(source)
    for i in range(len(input)-1,-1,-1):
        values = ord(input[i]) - ord(source[0])
        dec_value = dec_value + values*(len_source**j)
        j +=1
    print ("dec_value:",dec_value)
        
    result = []
    re = 1
    
    len_target = len(target)
    while re != 0:   
        #print ("111")
        re = dec_value/len_target
        se = dec_value%len_target
        dec_value = dec_value/len_target
        result.append(target[se])
        
    #print (result)
    #tem = list(result)
    # print ("tem",tem)
    result.reverse()
    # print ("tem1",tem)
    tem = "".join(result)

    return tem
if __name__ == "__main__":
	convert("15", "0123456789", "01")	