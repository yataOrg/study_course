#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
class World(str):

	def __eq__(self, other):
		return len(self) == len(other)

w1 = World('abc')
w2 = World('def')

print("{} == {} ? {}".format(w1, w2, w1 == w2))
print("{} == {} ? {}".format('abc', 'def', 'abc' == 'def'))

'''

'''
class Singleton(object):

	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
		return cls._instance

'''

'''
class Apple(object):

	def __init__(self, name, size):
		self.name = name
		self.size = size

	def __str__(self):
		return '{}:{}'.format(self.name, self.size)

print(Apple('A', '20kg'))
'''

'''
class Apple(object):

	def __init__(self, name, size):
		self.name = name
		self.size = size

	def __getattr__(self, name):
		return self.name

	def __setattr__(self, name, value):
		self.__dict__[name] = 'apple - {}'.format(value)

a = Apple('A', '100kg')
print(a.__dict__)
'''










