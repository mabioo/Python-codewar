# The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3
# 
def rgb(r, g, b):

	def format_rgb(a):
		if a.startswith("-"):
			print ("test")
			return "00"
		b = a.replace("0x","")
		if len(b)< 2:
			return ("0"+b)
		elif len(b) >2:
			return "FF"
		else:
			return b
	return (format_rgb(hex(r))+format_rgb(hex(g))+format_rgb(hex(b))).upper()


if __name__ == "__main__":
	print (rgb(-20,275,125))

#best solution:
#def rgb(r, g, b):
    # round = lambda x: min(255, max(x, 0))  #booom,cut the number of 0~255
    # return ("{:02X}" * 3).format(round(r), round(g), round(b))