#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-09-29 10:03:44
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-09-30 14:56:05

# import os, sys

# os.chdir('/usr/local/var/log')

# print("当前的路径是 %s" % (os.getcwd(), ))

# fd = os.open("/tmp", os.O_RDONLY)

# os.fchdir(fd)

# print("当前的路径是 %s" % (os.getcwd(), ))

# os.close(fd)
# 
# 





# import os, sys

# # 打开文件
# fd = os.open( "/usr/local/var/log/azhu.log", os.O_RDWR|os.O_CREAT)


# # 使用 ftruncate() 方法
# os.ftruncate(fd, 10)

# # 读取内容
# os.lseek(fd, 0, 0)
# str = os.read(fd, 100)
# print ("读取的字符串是 : ", str)

# # 关闭文件
# os.close( fd)

# print ("关闭文件成功!!")
# 


a = 10

def run(a):
	a = a + 1
	print(a)

run(10)


