#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yata
# @Date:   2019-05-28 09:06:14
# @Last Modified by:   yata
# @Last Modified time: 2019-05-29 19:12:00

'''
python3 -c "import sys; print(sys.path)"
'''

a = b =c = 5

a1, b1, c1 = 1, 2, 3
print(a1, b1, c1)

'''
python3的基本数据类型
Number
String
List
Tuple
Set
Dictionary

不可变类型 Number String Tuple
可变类型 List Set Dictionary
'''

# type 查看类型

a = '123'
b = 123
c = True
d = 3.14
e = 4 + 3j

print(type(e))

'''
type() 不会认为子类是一种父类类型
isinstance() 会认为子类是一种父类类型
'''

class A:
	def main():
		print("aaa")

class B(A):
	def main():
		print("bbb")

print(type(A()) == A)
print(isinstance(A(), A))

print(type(B()) == A)
print(isinstance(B(), A))

'''
>>>5 + 4  # 加法
9
>>> 4.3 - 2 # 减法
2.3
>>> 3 * 7  # 乘法
21
>>> 2 / 4  # 除法，得到一个浮点数
0.5
>>> 2 // 4 # 除法，得到一个整数
0
>>> 17 % 3 # 取余 
2
>>> 2 ** 5 # 乘方
32
'''

# 加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，紧跟的数字为复制的次数。实例如下：
# Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
# 另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行

# 列表
list0 = ['a', 'b', 'c', 'd', 'e']
list1 = [1, 2, 4, 5, 3]

print(list0 * 2)
print(list0 + list1)

# 翻转字符串
a = 'abcdefg'
reverse_a = a[-1::-1]

# CPython、IPython、Jython、PyPy 等

# 多行注释
# ''' ''' """ """

# 获取函数内的多行注释

def get_doc():
	'''
	我叫卡卡西
	'''
	print(get_doc.__doc__)

get_doc()

'''
按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
a & b) 输出结果 12 ，二进制解释： 0000 1100
---
按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
(a | b) 输出结果 61 ，二进制解释： 0011 1101
---
按位异或运算符：当两对应的二进位相异时，结果为1
^	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001
---
按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1
(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
'''

# is 是判断两个标识符是不是引用自一个对象
#  id() 函数用于获取对象内存地址。

'''
python支持三种不同的数值类型 整型 浮点型 复数  python3 整型是没有大小限制的 所以没有python3 的 long 类型

'''
import random
a = random.choice(range(10))
print(a)

'''
random.shuffle(range(5))
print(random.sample(['123','abc',52,[1,2]],2))  #随机返回参数列表中任意两个元素，参数二指定返回的数量
print(random.choice(['123','abc',52,[1,2]]))    #随机返回参数列表中任意一个元素
print(random.randrange(1,10,2))   #随机一个大于等于1且小于等于10之间的奇数，其中2表示递增基数
print(random.randint(1,5))  #随机一个大于等于1且小于等于5的整数
print(random.uniform(0,9))   #随机一个大于0小于9的小数
print(random.random())  #随机大于0 且小于1 之间的小数
'''

# 验证码生成器
def get_code():
	code = ''
	for i in range(4):
		ran1 = random.randint(0, 9)
		ran2 = chr(random.randint(65, 90))
		add = random.choice([ran1, ran2])
		code = ''.join([code, str(add)])

	return code

c = get_code()
print(c)


'''
函数	描述
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()	随机生成下一个实数，它在[0,1)范围内。
seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
'''



