#Find the missing letter

# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.

# Example:
# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'

def find_missing_letter(text):
	for i in range(len(text)):
		if text[i+1] != chr(ord(text[i])+1):
			return chr(ord(text[i])+1)


if __name__ == "__main__":
	print (find_missing_letter("abce"))

#best solutions:
# def find_missing_letter(chars):
 #    n = 0
 #    while ord(chars[n]) == ord(chars[n+1]) - 1:
 #        n += 1
 #    return chr(1+ord(chars[n]))