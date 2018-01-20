class Dictionary:
    def __init__(self,words):
        self.words=words


    #map_in = []
    def map_increse(self,temp):
        map_in =[]
        j =len(temp)-1
        while j >=1:
            map_in.append(ord(temp[j])-ord(temp[j-1]))
            j = j-1
        #map_in.append("$$")
        print("map_in:",map_in)
        return sum(map_in)

    def hello(self):
        print ("Hello Marble!! Cheer up!!!!")

    def find_most_similar(self,term):
        inscrease =  [self.map_increse(i) for i in self.words]
        print ("incresse:",inscrease)
        print ("term:",self.map_increse(term))
        termwords = self.map_increse(term)
        temp = abs(termwords -inscrease[0])
        i=0
        tempIndex = 0
        while i<len(inscrease):
            if abs(termwords-inscrease[i]) <temp:
                tempIndex = i
                temp = abs(termwords -inscrease[i])
                #print ("tempIndex:%d,temp:%d",(tempIndex,temp))
            i = i+1
        return self.words[tempIndex]

if __name__ =="__main__":
    words=['riyhpvimgaliuxr', 'clxmqmiycvidiyr', 'osbednerciaai', 'xikoctmrhpvi', 'emvquxrvvlvwvsi', 'dyhxgviphoptak', 'iroezmixmberfr', 'cwhyyzaorpvtnlfr', 'dihhiczkdwiofpr', 'qifwqgdsijibor', 'cpnqknjyviusknmte', 'jcocndjkyb', 'sefsknopiffajor', 'npyrgrpbdfqhhncdi', 'nnsoamjkrzgldi', 'tdvibqccxr', 'ntwmwwmicnjvhtt', 'ucxmdeudiycokfnb', 'ajacizfrgxfumzpvi', 'hkldhadcxrjbmkmcdi', 'zqdrhpviqslik', 'fgtrjakzlnaebxr', 'mhmkakybpczjbb', 'ggcvrtxrtnafw', 'karpscdigdvucfr', 'ppctybxgtleipb', 'qojfrlhufr', 'xffrkbdyjveb', 'jhjyasikwyufr', 'cfvruditwcxr', 'xuwahveztwoor', 'znystgvifufptxr', 'loogviwcojxgvi', 'fxpvfhfrujjaifr', 'vkholxrvjwisrk', 'pdyjrkaylryr', 'hirldidcuzbyb', 'tklquxrnhfiggb', 'psaysnhfrrqgxwik', 'ljxzjjorwgb', 'kqijoorfkejdcxr', 'iqkyztorburjgiudi', 'pxyousorusjxxbt', 'eglanhfredaykxr', 'lnjhrzfrosinb', 'hwzsemiqxjwfk', 'hrwuhmtxxvmygb', 'afirbipbmkamjzw', 'fxjskybblljqr', 'xrgdgqfrldwk']
    test_dict=Dictionary(words)
    print ("apple:",test_dict.find_most_similar("rkacypviuburk"))