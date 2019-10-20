#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-08 12:03:04
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-20 11:42:40

'''
import MySQLdb

db = MySQLdb.connect('localhost', 'root', '123456', 'getyii', charset='utf8')

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version is %s" % (data, ))
db.close()
'''

class A(object):
    """
    Class A.
    """

    a = 0
    b = 1

    def __init__(self):
        self.a = 2
        self.b = 3

    def test(self):
        print('a normal func')

    @staticmethod
    def static_test(self):
        print('a static func')

    @classmethod
    def class_test(self):
        print('a calss func')


if __name__ == "__main__":
	obj = A()
	print(A.__dict__)
	print("$$$$$" *3 + "\n")
	print(obj.__dict__)

