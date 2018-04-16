# -*- coding: utf-8 -*-
# 爬取codewar上的个人的注册时间
#Task: Write a function get_member_since which accepts a username from someone 
#at Codewars and returns an string containing the month and year separated 
# by a space that they joined CodeWars.

###If you want/don't want your username to be in the tests, ask me in the 
# discourse area. There can't be too many though because the server may 
# time out.


#Example:

# >>> get_member_since('dpleshkov')
# Jul 2016
# >>> get_honor('jhoffner')
# Oct 2012
#Libraries/Recommendations:

##Python:

urllib.request.urlopen: Opens up a webpage.
re: The RegEx library for Python.
bs4(BeautifulSoup): A tool for scraping HTML and XML.
Python 2 is not working for this kata. :(
#Notes:

While this kata is in beta, please vote/downvote on it and give your rank assessment.
Feel free to voice your comments and concerns in the discourse area.

from bs4 import BeautifulSoup
import urllib2
import re


def get_member_since(username):
	urlname = "https://www.codewars.com/users/" + username
	print (urlname)
	try:
	    html = urllib2.urlopen(urlname)
	except  urllib2.URLError as e:
	    print e
	print ("html:",html)
	bsObj = BeautifulSoup(html.read())
	test = bsObj.select(".stat")

	i = 0
	while test[i].b.string != "Member Since:":
		i+=1

	tem = list(test[i])
	print str(tem[1])

if __name__ =="__main__":
	get_member_since("kazk")

