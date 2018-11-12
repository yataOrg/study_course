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

list_2d = [[0 for x in range(5)] for i in range(5)]
print(list_2d)

list_2d_2 = [[0 for x in range(5)] for i in range(5)]
print(list_2d_2)















