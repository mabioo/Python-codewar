# The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples:

# "din" => "((("

# "recede" => "()()()"

# "Success" => ")())())"

# "(( @" => "))(("

def duplicate_encode(word):
    word = word.upper()
    indexList =  ([ word.count(i) for i in word ])
    target = ''
    print (word.count("S"))
    print (indexList)
    for i in range(len(indexList)):
    	if indexList[i] == 1:
    		target = target +"("
    	else:
    		target = target +")"
    return target



if __name__ == "__main__":
	print (duplicate_encode("Success"))


#best solution:
# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])