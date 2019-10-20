#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-20 09:05:30
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-20 10:12:00

import time
import sys

"""使用多个装饰器装饰一个函数"""

def azhu(f):

	def wrapper(*args, **kwargs):
		start_time = time.time()
		f(*args, **kwargs)
		end_time = time.time()
		execution_time = (end_time - start_time) * 1000
		print("time is cost %d ms" % (execution_time,))
		print("out of func_name 0-- %s" % sys._getframe().f_code.co_name)
	return wrapper

def azhu1(f):

	def wrapper(*args, **kwargs):
		print("i am runing")
		f(*args, **kwargs)
		print("out of func_name 1-- %s" % sys._getframe().f_code.co_name)
	return wrapper


@azhu
@azhu1
def f(name, song):
	print("my name is %s" % name)
	print("the name of my song is %s" % song)

if __name__ == "__main__":
	f("azhu", "The moon stands for my heart")

