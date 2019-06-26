#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yata
# @Date:   2019-06-18 20:32:14
# @Last Modified by:   yata
# @Last Modified time: 2019-06-18 20:44:23

class MyNumbers:

	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		if self.a <= 20:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration


myClass = MyNumbers()
myIter = iter(myClass)

for x in myIter:
	print(x)
