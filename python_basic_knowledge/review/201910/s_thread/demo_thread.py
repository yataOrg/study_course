#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-09 22:31:53
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-10 08:36:04

import time
import _thread as thread

# 为线程定义一个函数
def print_time(thread_name, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print("%s : %s" % (thread_name, time.ctime(time.time())))


try:
	thread.start_new_thread(print_time, ('Thread_name_1', 2))
	thread.start_new_thread(print_time, ('Thread_name_2', 5))
except:
	print("Error: unable to start thread")

while 1:
	pass