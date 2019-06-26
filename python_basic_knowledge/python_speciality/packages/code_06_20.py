#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yata
# @Date:   2019-06-20 17:09:01
# @Last Modified by:   yata
# @Last Modified time: 2019-06-20 18:46:55


# 面对对象开发模式  包

# 类的继承 定义 调用 实例化的方式


class MysqlObj(object):

	host = ''
	port = 3306
	user = ''
	pwd = ''

	# 私有变量
	__password = '123456'

	# 构造函数 初始化
	def __init__(self, host, port, user, pwd):
		# 数据库连接 逻辑
		self.host = host
		# print("用初始化的时候 传递的参数 进行数据库连接")


	def insert(self, data):
		pwd = self.__password
		print('数据库插入一条数据 %s' % data )

	def save(self, data):
		print('保存数据')

	# 私有方法
	def __msg(self):
		return '我是结尾'
	
	def update1(self):

		update_data = self.__msg()
		print('末尾都加上---' + update_data)


	def __del__(self):
		self.host = ''
		self.port = ''
		self.user = ''
		#print("我是析构方法，垃圾回收")

	def __repr__(self):

		return 'dfdfdfdfdfd'


	def __str__(self):

		return '类的描述 我是数据库操作类'


# 实例化
# mysqlObj = MysqlObj('127.0.0.1', 3306, 'root', '123456')
# mysqlObj.insert("一篇文章")

mysqlObj = MysqlObj('127.0.0.1', 3306, 'root', '123456')


mysqlObj.update1()
print(mysqlObj.__password)



'''
class Vector:

    def __init__(self, a, b):
    	self.a = a
    	self.b = b
 
    def __str__(self):
    	return 'Vector (%d, %d)' % (self.a, self.b)
   
    def __add__(self,other):

    	# 实例化
    	return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)

v2 = Vector(5,-2)


print(v1 + v2)
'''







