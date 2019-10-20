#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-20 08:23:47
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-20 09:04:50


import time
import sys

"""无固定参数的装饰器"""

def azhu(f):

	def wrapper(*args, **kwargs):
		start_time = time.time()
		f(*args, **kwargs)
		end_time = time.time()
		execute_time = (end_time - start_time) * 1000
		print("time is %d ms" % (execute_time,))
	return wrapper


@azhu
def f0(a, b):
	print("当前函数名称是 %s" % sys._getframe().f_code.co_name)
	print("let's go")
	time.sleep(1)
	print("this result is %d" % (a + b,))

@azhu
def f1(a, b, c):
	# 函数内部获取函数名称
	print("当前函数名称是 %s" % sys._getframe().f_code.co_name)
	print("let's go")
	time.sleep(1)
	print("this result is %d" % (a + b + c,))

@azhu
def f2(name='azhu', clothes='white', shoes='white'):
	print("当前函数名称是 %s" % sys._getframe().f_code.co_name)
	print("let's go")
	time.sleep(1)
	print("i am %s, my clothes is %s, my shoes are %s" % (name, clothes, shoes))


if __name__ == "__main__":
	f0(1, 2)
	f1(1, 2, 3)
	f2(clothes="blue", name='xiaoMing', shoes='dark')


