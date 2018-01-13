# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.

# Examples:

# # returns "theStealthWarrior"
# to_camel_case("the-stealth-warrior") 

# # returns "TheStealthWarrior"
# to_camel_case("The_Stealth_Warrior")

def to_camel_case(text):
    if text =='':
        return ''
    for i in range(len(text)):
    	if text[i] == '_' or text[i] == '-':
    		del(text[i])
    		text[i+1].replace("")
    return text
    #return "".join(([text[i+1].upper() if text[i] == '-' or text[i] == '_' else text[i] for i in range(0,len(text)) ]))

if __name__ == "__main__":
	print (to_camel_case("the_stealth_warrior"))

