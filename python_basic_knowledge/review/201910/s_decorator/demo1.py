#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-20 07:37:58
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-20 08:18:19

"""
python装饰器 就是用于拓展原来函数功能的一种函数，目的是在不改变原函数名(或类名)的情况下，给函数增加新的功能。
通常我们修改或者扩展一个函数或者类的功能都是需要在原来的基础上进行修改的，这种是侵入式的，对目标进行了修改和破坏。
装饰器是一种设计模式，他不需要修改和破坏目标的内容，即可给目标扩展各种不同的功能，它是优雅的，简单的。 

装饰器函数的特殊之处在于它的返回值也是一个函数，这个函数是内嵌"原"函数的函数。
装饰器特征:
1.不修改被装饰函数的调用方式 
2.不修改被装饰函数的源代码
"""

import time

"""无参数装饰器"""
def azhu(f):
	def wrapper():
		start_time = time.time()
		f()
		end_time = time.time()
		execution_time = (end_time - start_time) * 1000
		print("time is %d ms" % (execution_time,))
	return wrapper

@azhu
def f():
	print("hello")
	time.sleep(1)
	print("world")

if __name__ == '__main__':
	f()









