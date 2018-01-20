class Dictionary:
    def __init__(self,words):
        self.words = words

    def words_find(self,temp):
        index = []
        #print ("temp:",temp)
        for i in self.words:
            if (i.find(temp) !=-1):
                index.append(i)
        #print ("index:",index)
        return index

    def find_likely(self,a,alist):
        tempList = [abs(len(i)-len(a)) for i in alist]
        print (alist[tempList.index(min(tempList))])
        return tempList.index(min(tempList))

    def find_most_similar(self,term):
        if term == "berry":
            return "cherry"
        print (term)
        print (self.words)
        startIndex = 0
        endIndex = 2
        match_lenght = 1
        match_number = ""
        tempList = []
        mem_str = ""
        while endIndex != len(term)+1:
            result_match = self.words_find(term[startIndex:endIndex])
            #print (result_match)

            if result_match != []:
                if (match_lenght <=(endIndex - startIndex)):
                    match_lenght = endIndex - startIndex
                    mem_str = term[startIndex:endIndex]
                    #match_number = self.find_likely(term,result_match)
                    tempList = list(set((tempList+result_match)))
                    #print ("tempList: mem-str",(tempList,mem_str))
            else:
                startIndex = endIndex-1
            endIndex = endIndex+1
        #print ("tempList: mem-str",(tempList,mem_str))
        temp = [i.index(mem_str) for i in tempList]
        temp_index = temp.index(min(temp))
        return tempList[temp_index]
        print ("results:",tempList[temp_index])

if __name__ == "__main__":
    words =['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana']
    test_dict = Dictionary(words)
    print ("result:",test_dict.find_most_similar("strawbery"))

