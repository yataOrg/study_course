#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-20 12:26:32
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-20 12:29:37

import inspect

def azhu():

	print("hello azhu")

# 在函数外部获取函数名称，用.__name__获取

print(azhu.__name__)

# 函数内部获取当前函数名称，用sys._getframe().f_code.co_name方法获取
# 获取类名称self.__class__.__name__
# 使用inspect模块动态获取当前运行的函数名（或方法名称）

def get__function_name():
    '''获取正在运行函数(或方法)名称'''
    return inspect.stack()[1][3]

def yoyo():
    print("函数名称：%s"%get__function_name())

class Yoyo():
    def yoyoketang(self):
        '''# 上海-悠悠 QQ群：588402570'''
        print("获取当前类名称.方法名：%s.%s" % (self.__class__.__name__, get__function_name()))

if __name__ == "__main__":
    yoyo()
    Yoyo().yoyoketang()

