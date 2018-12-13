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

# ---
'''
import hello
c = dir(hello)
print(c)
'''

# ---
'''
from urllib import request

response = request.urlopen("http://www.baidu.com/")
fi = open("demo.txt", 'w')
page = fi.write(str(response.read()))
fi.close()
'''
# ---
'''
import pickle

data = ['a', 'b', 'c', 'd']
data1 = {'a': 'a1', 'b': 'b1', 'c': 'c1', 'd': 'd1'}
p_str = pickle.dumps(data1)
print(p_str)
'''

# ---
'''
import os, sys

f = open('txt', 'a')
os.dup2(f.fileno(), 1)
f.close()

print('google')
print('app')
'''
# ---
'''
import os

m, s = os.openpty()
print(m)
print(s)
t = os.ttyname(s)
print(m)
print(t)
'''

# ---
'''
import os
print(os.pathconf_names)
'''

# ---
'''
import re

phone = "0321-18521568316 # this is an telephone number"

num = re.sub('#.*$', '', phone, 0)

num1 = re.sub(r'\D', '', phone, 0)
print(num)
print(num1)
'''

# ---
'''
import re

def double(matched):
	value = int(matched.group('value'))
	return str(value*2)

s = 'A23G4HFD567'
num = re.sub('(?P<value>\d+)', double, s)
print(num)
'''

# str = r'这个价格住这样的房间真的很便宜，尤其前台的小院子很大，没事还可以到前台来泡茶喝，很悠闲，无聊时跟店家姐姐聊聊天，很棒！'
# a = str.strip().split(' ')
# print(a)

# ---
'''
import os
for i ,item in enumerate(os.environ):
	print("this is %s and %s" % (i, item))
'''

# ---
'''
import _thread, time

def print_time(threadName, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		# print("%s: %s" % (threadName, time.ctime(time.time())))
		print("{0}:{1}".format(threadName, time.ctime(time.time())))

# 创建2个线程
try:
	_thread.start_new_thread(print_time, ('Thread-1', 2))
	_thread.start_new_thread(print_time, ('Thread-2', 4))

except:
	print('Error 无法启动线程')
'''

# --- 线程同步
'''
import threading, time

exitFlag = 0

class myThread(threading.Thread):

	def __init__(self, threadId, name, counter):
		threading.Thread.__init__(self)
		self.threadId = threadId
		self.name = name
		self.counter = counter

	def run(self):
		print("开始线程" + self.name)
		print_time(self.name, self.counter, 5)
		print("退出线程" + self.name)


def print_time(threadName, delay, counter):
	while counter:
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print("{0}: {1}".format(threadName, time.ctime(time.time())))
		counter -= 1

thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('退出主线程')
'''

# ---

'''
import threading, time

class myThread(threading.Thread):

	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):
		print('开启线程: ' + self.name)
		# 获取锁，用于线程同步
		threadLock.acquire()
		print_time(self.name, self.counter, 3)
		# 释放锁，开启下一个线程
		threadLock.release()

def print_time(threadName, delay, counter):
	while counter:
		time.sleep(delay)
		print("%s: %s" % (threadName, time.ctime(time.time())))
		counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
	t.join()

print('退出主线程')
'''

# ---
'''
import threading, Queue as queue, time

exitFlag = 0

class myThread(threading.Thread):

	def __init__(self, threadId, name, q):

		threading.Thread.__init__(self)
		self.threadId = threadId
		self.name = name
		self.q = q


	def run(self):

		print('开启线程:' + self.name)
		process_data(self.name, self.q)
		print('结束线程:' + self.name)


def process_data(threadName, q):

	while not exitFlag:
		queueLock.acquire()
		if not workQueue.empty():
			data = q.get()
			queueLock.release()
			print('%s processing %s' % (threadName, data))
		else:
			queueLock.release()

		time.sleep(1)


threadList = ['Thread-1', 'Thread-2', 'Thread-3']
nameList = ['One', 'Two', 'Three', 'Four', 'Five']
queueLock = threading.Lock()
workQueue = queue.Queue(10)

threads = []
threadId = 1

# 创建新线程
for tName in threadList:
	thread = myThread(threadId, tName, workQueue)
	thread.start()
	threads.append(thread)
	threadId += 1

# 填充队列
queueLock.acquire()
for work in nameList:
	workQueue.put(work)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
	pass


# 通知线程是时候退出
exitFlag = 1

for t in threads:
	t.join()

print('退出主线程')
'''

#---
'''
import time

t = time.localtime()
print("asctime = %s" % (time.asctime(t)))
'''

# ---
'''
import time


sys_time = time.perf_counter()
pro_time = time.process_time()
print("{}----{}".format(sys_time, pro_time))
'''

# ---
'''
import time

# print("ctime() {}".format(time.ctime()))

local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

local_time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(2995508609.34375))
print(local_time1)
'''

import calendar

# print(calendar.month(2018, 6, w=2, l=1))
# print(calendar.monthrange(2018, 5))
# print(calendar.calendar(2018, w=2, l=1, c=6))
# print(calendar.calendar(2018, w=2, l=1, c=5))


import pandas as pd

df = pd.read_excel("./../limihu.xlsx")
print(df.shape)























