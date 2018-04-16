if __name__ == "__main__":
    count_slo = int(raw_input())
    count_blo = []
    spec_info = []
    # count_slo = 2
    # count_blo = [3,11]
    # spec_info = [".X.","...XX....XX"]
    temp = count_slo
    while temp:
        count_blo.append(int(raw_input()))
        spec_info.append(str(raw_input()))
        temp -=1
    
    result = [0 for i in range(0,count_slo)]
    for i in range(0,count_slo):
    	j = 0
    	while j <= count_blo[i]-1 :
    		if spec_info[i][j] == ".":
    			result[i] += 1
    			j += 3
    		else: 
    			j +=1
    for i in range(len(result)):
    	print result[i]		
