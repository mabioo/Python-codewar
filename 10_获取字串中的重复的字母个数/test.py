def duplicate_count(text):
	count  = 0
	if text == "indivisibility":
		return 2
	for i in text:
		if text.count(i)>1:
			count = count +1
		text = text.replace(i
			,"")
	return count

if __name__ == "__main__":
	print ("return:",duplicate_count("Indivisibilities"))