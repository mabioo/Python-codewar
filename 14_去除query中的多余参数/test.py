# Complete the method so that it does the following:

# Removes any duplicate query string parameters from the url
# Removes any query string parameters specified within the 2nd argument (optional array)
# Examples:

# stripUrlParams('www.codewars.com?a=1&b=2&a=2') // returns 'www.codewars.com?a=1&b=2'
# stripUrlParams('www.codewars.com?a=1&b=2&a=2', ['b']) // returns 'www.codewars.com?a=1'
# stripUrlParams('www.codewars.com', ['b']) // returns 'www.codewars.com'

def strip_url_params(url, params_to_strip = []):
    #make a map for data
    specialMap = {}
    tempString = url
    for i in range(len(url)):
    	if (url[i] == "=") and (url[i-1] not in params_to_strip):
    		params_to_strip.append(url[i-1])
    		tempString = tempString[0:i-2]+tempString[i+2:]
    		specialMap[url[i-1]] = url[i+1]
    print (tempString)


if __name__ == "__main__":
	strip_url_params('www.codewars.com?a=1&b=2&a=2')



