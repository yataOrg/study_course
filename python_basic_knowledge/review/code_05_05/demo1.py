#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
class MyNumbers:

    def __init__(self):
        pass

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


if __name__ == "__main__":

    obj = MyNumbers()
    my_iter = iter(obj)
    for x in my_iter:
        print(x)
"""

'''
import sys

def fibonacii(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a+b
        counter += 1

f = fibonacii(10)

while True:
    try:
        print(next(f), end="\n")
    except StopIteration:
        sys.exit()
   

'''

# 列表推导式
def list_a():
    tem_a = ['a', 'b', 'c']
    end = [[x, x*2] for x in tem_a]
    return print(end)

def list_b():
    tem_b = ['a ', 'b ', 'c', 'd ']
    end = [o.strip() for o in tem_b if o != '']
    return print(end)

def list_c():
    tem_c1 = [1, 2, 4, 6, 8]
    tem_c2 = [0, 3, 7, 13, 15]
    end = [str(x) + '-' + str(y) for x in tem_c1 for y in tem_c2]
    end1 = [str(x) + '-' + str(y) for x in tem_c1 for y in tem_c2 if y > 0 if x > 1 ] 
    # end1 = [str(x) + '-' + str(y) for x in tem_c1 for y in tem_c2 if y > 0 and x > 1 ]
    return print(end, end1, sep='\n')







if __name__ == "__main__":
    # list_a()
    # list_b()
    list_c()

