#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yata
# @Date:   2019-05-28 09:06:14
# @Last Modified by:   yata
# @Last Modified time: 2019-06-26 10:06:04

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

a = 'hello world'
b = a.encode('UTF-8')
print(b)
print(type(b))

c = b.decode(encoding = 'UTF-8', errors = 'strict')
print(c)
print(type(c))


# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，
tup1 = (1, 2, 3)
tup2 = ('a', 'b', 'c')
tup3 = tup1 + tup2

# 清空字典 dict.clear()
# 删除字典 del dict del dict['abc']

'''
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''


a, b = 0, 1
while b < 1000:
	print(b, end='@')
	a, b = b, a+b


'''
#!/usr/bin/python3
 
import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
'''

'''
list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x)	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i])	从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear()	移除列表中的所有项，等于del a[:]。
list.index(x)	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x)	返回 x 在列表中出现的次数。
list.sort()	对列表中的元素进行排序。
list.reverse()	倒排列表中的元素。
list.copy()	返回列表的浅复制，等于a[:]。
'''

'''
from collections import deque
'''

































