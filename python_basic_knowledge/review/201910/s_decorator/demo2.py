#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-20 08:17:01
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-20 17:09:54










import time

"""固定参数装饰器"""
def azhu(f):

	def wrapper(a, b):
		start_time = time.time()
		f(a, b)
		end_time = time.time()
		execute_time = (end_time - start_time) * 1000
		print("cost time is %d" % (execute_time,))
	return wrapper

@azhu
def f(a, b):
	print("let's go")
	time.sleep(1)
	print("this result is %d" % (a+b,))

if __name__ == "__main__":
	f(1, 1)
