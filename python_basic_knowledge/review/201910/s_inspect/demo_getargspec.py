#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-20 11:47:48
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-20 12:26:12

'''
import inspect

def attr_from_locals(locals_dict):

	self = locals_dict.pop('self')
	args = inspect.signature(self.__init__.__func__)
	print(args.parameters)


class Foo(object):

	def __init__(self, *args, **kwargs):
		attr_from_locals(locals())

if __name__ == "__main__":
	f = Foo('Bar', color="yellow", num=1)

'''

import inspect

def get__function_name():
    '''获取正在运行函数(或方法)名称'''
    # print(inspect.stack()[1][2])
    return inspect.stack()[1][3]

def yoyo():
    print("函数名称：%s"%get__function_name())

class Yoyo():
    def yoyoketang(self):
        print("获取当前类名称.方法名：%s.%s" % (self.__class__.__name__, get__function_name()))

if __name__ == "__main__":
    yoyo()
    Yoyo().yoyoketang()