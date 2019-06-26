#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def foo():
	return 1, 2


x, y = foo()
print(x, y)

data0 = foo()
print(data0, data0[0])