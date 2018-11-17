#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
str = "hello world";
print(str[0:-1])
print(str[2:7])
input("\n\n按下 enter 键后退出")
'''

# import sys; x = 'hello world'; sys.stdout.write(x + '\n')

# print("adfaf")
# a, b, c = 1, 2, 3
# print(a, b, c)

'''
student = {'aa1', 'aa2', 'aa3'}
if 'aa2' in student:
	print('in')
else:
	print('not in')
'''

# set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
 
# print(a)
 
# print(a - b)     # a和b的差集
 
# print(a | b)     # a和b的并集
 
# print(a & b)     # a和b的交集
 
# print(a ^ b)     # a和b中不同时存在的元素

# ---
'''
import random
c = random.choice(range(10))
print(c)
'''

# ---
'''
str = "hello world"
middle_str = str.center(40, '*')
print(middle_str)
'''

# ---
'''
str = "yan zhi zpeng"
num = str.count('z', 0, -1)
print(num)
'''

# ---
'''
print("this is %#x" %  (1343434,))
print("abcdefg is %#o" % (43344334,))
print(bin(33333))
'''

'''
#必须引用如下库
from collections import Counter

#定义两个字符串变量

Var1 = "1116122137143151617181920849510"
Var2 = "1987262819009787718192084951"

#以字典的形式，输出每个字符串中出现的字符及其数量
print (Counter(Var1))
print (Counter(Var2))
'''

'''
list_2d = [[0 for x in range(5)] for i in range(5)]
print(list_2d)

list_2d_2 = [[0 for x in range(5)] for i in range(5)]
print(list_2d_2)
'''

# ---
'''
tup = "a", "b", "c", "d"
print(type(tup))
print(tup)
'''

# ---
'''
c = {"google", "baidu", "ali"}
d = {"qtt", "pingan", "baidu", "google"}
# st_end = c.intersection_update(d)
# st_end = c.difference(d)
c.difference_update(d)
print(len(c))
'''
# ---
'''
a = {"lidan", "zhuenni", "zhuyuhui"}
b = {"aaa"}

c = a.isdisjoint(b)
print(c)
'''

# ---
'''
a = {'a', 'b', 'c', 'd'}
b = {'a', 'b', 'c', 'd', 'f'}

st_end = a.issubset(b)
print(st_end)
'''

# ---
'''
a,b = 0, 1
while b < 1000:
	print(b)
	a, b = b, a+b
'''

'''
a = 10; b = 18; c = 22
print(a,b,c)
'''

# ---
'''
def fab(n):
	
	if n < 1:
		print("输入有误!")
		return -1
	if 1 == n or 2 == n:
		return 1

	else:
		return fab(n - 1) + fab(n - 2)

print(fab(6))
'''

# ---
'''
list = ['a', 'b', 'c', 'd', 'e']
item = iter(list)
print(next(item))
print(next(item))
print(next(item))
'''

# ---
'''
list = ['a', 'b', 'c', 'd', 'e']
list1 = ('a', 'b', 'c', 'd', 'e')
list2 = {'a': 'a1', 'b': 'b1'}
it = iter(list1)
for x in it:
	print(x)
'''
# ---
'''
class MyNumbers:

	def __iter__(self):
		self.a = 1
		return self


	def next(self):
		if self.a <= 20:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration


item = MyNumbers()
it = iter(item)
for x in it:
	print(x)
'''

# ---
'''
class Fab(object):

	def __init__(self, max):
		self.max  = max
		self.n, self.a, self.b = 0, 0, 1

	def __iter__(self):
		return self

	def next(self):
		if self.n < self.max:
			r = self.b
			self.a, self.b = self.b, self.a + self.b
			self.n = self.n + 1
			return r

		raise StopIteration()

for x in Fab(50):
	print(x)
'''

# ---
'''
def Fab(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1

for x in Fab(55):
	print(x)
'''

# ---
'''
from collections import deque
queue = deque(['a1', 'b1', 'c1', 'd1'])
queue.append("e1")
queue.append('f1')
# print(queue.popleft())
print(queue.popleft())
'''

# ---
'''
import sys

print("命令行参数如下：")
for i in sys.argv:
	print(i)

print("\n\npython3的路径为:", sys.path, '\n')
'''

### ---
'''
import hello
c = dir(hello)
print(c)
'''













