class Token(object):
    def __init__(self,char,type):
        self.char = char
        self.type = type

    def __str__(self):
        return "Token(chars='%s', type='%s')"%(self.char,self.type)


class Simplexer(object):

    def __init__(self, expression):
        print ("expression:",expression)
        self.identi_list = []
        start = 0 
        strs = False
        self.iter_index = 0
        for i in range(len(expression)):            
            if expression[i] >="a" and expression[i]<= "z" and i != len(expression) -1:
                if strs != True:
                    start = i
                    strs = True
                continue
            elif strs == True:
                self.identi_list.append(expression[start:i])
                strs = False
            self.identi_list.append(expression[i])

        print ("identi_list:",self.identi_list)
    
    def __iter__(self):
        return self
                
    def __next__(self):
        #there is processing the identi_list, every time went to the method of the 
        # next(), we should return a string.
        map_str = {
            "oeprater":["+", "-", "*", "/", "%", "(", ")",  "="],
            "boolean":["True","False"],
            "keywords":["if", "else", "for", "while", "return", "func", "break"],
            "integer": ["0","1","2","3","4","5","6","7","8","9"]
        }
        
        result = []
        try:
            for key in map_str:
                if self.identi_list[self.iter_index] in map_str[key]:
                    self.iter_index += 1
                    result.append(Token(self.identi_list[self.iter_index],key))
                    return result[0]
            if self.identi_list[self.iter_index] == " ":
                self.iter_index += 1
                result.append(Token(self.identi_list[self.iter_index],"whitespace"))
                return result[0]
            else:
                result.append(Token(self.identi_list[self.iter_index],"identifier"))
                return result
            self.iter_index += 1
        except IndexError:
            raise StopIteration


if __name__ =="__main__":
    a = Simplexer("x")
    for i in range(3):
        print a.__next__()
