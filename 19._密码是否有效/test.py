# In this example you have to validate if a user input string is alphanumeric. The given string is not nil, so you don't have to check that.
#
# The string has the following conditions to be alphanumeric:
#
# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces/underscore

def alphanumeric(string):
    if " " in string:
        return False
    up = list(range(ord("A"),ord("Z")+1))
    min = list(range(ord("a"),ord("z")+1))
    numbers = list(range(ord("0"),ord("9")+1))
    for i in string:
        j = ord(i)
        if j not in up and j not in min and j not in numbers:
            return False
        else:
            return True

if __name__ == "__main__":
    print (alphanumeric(" 123"))

#best solutions:
# import re
#
# def alphanumeric(string):
#     return bool(re.search(r'^[0-9a-zA-Z]+$', string))