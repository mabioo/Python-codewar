# -*- coding:utf-8 -*-
#协程的简单实现

def coroutine(pattern):
	print "Please input the string:"
	while True:   #注意将需要协程实现的放在永循环中
		line = yield   #yield 不会像生成器中使用一样给到一个数据，协程的数据是从外面send进来的
		if pattern in line:
			print line


if __name__ == "__main__":

	a= coroutine("test")
	next(a)
	a.send("aaa test")
	a.send("this is other string of test")
	a.close()
