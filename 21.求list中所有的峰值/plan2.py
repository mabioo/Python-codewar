def pick_peaks(arr):
    inscrase = [arr[i]-arr[i-1] for i in range(1,len(arr))]
    print (inscrase)
    targetsict = {
        "pos":[],
        "peaks":[]
    }
    tempIndex = 0
    for i in range(1,len(inscrase)):
        if inscrase[i] == 0 and inscrase[i-1] >0:
            tempIndex = i
        if inscrase[i-1] ==0 and inscrase[i] <0 and tempIndex != 0:
            targetsict["pos"].append(tempIndex)
            targetsict["peaks"].append(arr[tempIndex])
            tempIndex = 0
        if inscrase[i-1] >0 and inscrase[i]<0:
            targetsict["pos"].append(i)
            targetsict["peaks"].append(arr[i])
    return targetsict
if __name__ == "__main__":
    print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]))

# def pick_peaks(arr):
# pos = []
# prob_peak = False
# for i in range(1, len(arr)):
#     if arr[i] > arr[i-1]:
#         prob_peak = i
#     elif arr[i] < arr[i-1] and prob_peak:
#         pos.append(prob_peak)
#         prob_peak = False
# return {'pos':pos, 'peaks':[arr[i] for i in pos]}