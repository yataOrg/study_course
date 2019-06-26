#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yata
# @Date:   2019-06-19 10:24:45
# @Last Modified by:   yata
# @Last Modified time: 2019-06-19 11:48:38

'''必需参数
关键字参数
默认参数
不定长参数
'''

# 没有参数
'''
def onePlay():

	a = 1
	return a+1

myMethod()
'''

# 普通有参数

'''
def onePlay(doing):

	print(doing, " ball")
	return  # None

onePlay('me')
'''

# 关键字参数 调用的时候不按照顺序 关键字给出

'''
def onePlay(name, age):

	print("name is", name)
	print("age is", age)
	return

onePlay(age = 22, name = 'peng')
'''

# 不定长参数 * tuple (3,)

'''
def someMethod(name, age, *some):

	print("name ", name)
	print("age ", age)
	print(some)
	if len(some) >= 2:
		print("第一个扩展参数是", some[0])
		print("第二个扩展参数是", some[1])
	return

someMethod('hhh', 18, 55, 66, 77)
'''

### 不定长关键字参数 dict {}

'''
def someMethod(name, age, **some):

	print('name ', name)
	print('age ', age)
	print(some)
	if 'height' in some:
		print(some['height'])
	return

someMethod(name = 'peng', age = 22, height1=111, close=3)
'''

### 匿名函数
'''
oneList = lambda x,y,z, *a: x + y + z +  a[0] + a[1]
print(oneList(1,2,3, 4, 5))
'''

'''
a = list(filter(lambda x:x%2,range(10)))

print(a)
'''

# 全局变量

'''
x = 100 # 全局变量

def test(y):

	a = 10  # 局部变量
	return x + y + a

def test1(b):

	a1 = test(10)
	return b + a1

print(test1(5))
'''




# 鸟类
'''
class Bird:

    """一个简单的类实例"""
    fly = '飞'
    run = '跑'

    def play(self):
    	msg = "鸟类可以 " + self.fly + " " + self.run
    	print(msg)
    	return

# 实例化
myObj = Bird()

myObj.play()
'''


## 动物类
class Animal:

	name = '名字'
	walk = '行走'
	age = '年龄'

	def walk(self):
		print("我可以行走")

	def name(self):
		print("我有自己的年龄")

	def eat(self):
		print("我可以吃食物")

	def show(self):
		print("我叫 " + self.name)

# 鸟类
# 继承 遗产
# 多态
class Bird(Animal):
	
	name = '鸟类'

	def fly(self):
		print("我可以飞")

	def eat(self):
		print("我可以吃昆虫")


class Monkey(Animal):
	
	name = "猴子"

	def play(self):
		print("我在花果山水帘洞")

	def eat(self):
		print("我可以吃桃子")

# 实例化
myBird = Bird()

myBird.fly()
myBird.eat()
myBird.show()

print('-------\r')
monkey = Monkey()
monkey.play()
monkey.eat()
monkey.show()



















