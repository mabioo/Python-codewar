
class Token(object):
	def __init__(self,char,type):
		self.char = char
		self.type = type

	def __str__(self):
		return "Token(chars='%s', type='%s')"%(self.char,self.type)

if __name__ =="__main__":
	a = Token("1","integer")
	print a 