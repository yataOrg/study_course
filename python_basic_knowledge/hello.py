#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# def hello(name):
# 	print("hello : %s" % name)
#
#
# if __name__ == "__main__":
# 	print("我自几个运行了")
# else:
# 	print("你要让我帮你做事情？")


import pickle

dataList = [
    [1, 1, 'yes'],
    [1, 1, 'yes'],
    [1, 0, 'no'],
    [0, 1, 'no'],
    [0, 1, 'no']
];

dataDic = {
    0: [1, 2, 3, 4],
    1: ('a', 'b'),
    2: {'c': 'yes', 'd': 'no'}
}

fw = open('pickle.txt', 'rb')
# pickle.dump(dataList, fw, -1)

# pickle.dump(dataDic, fw)
c = pickle.load(fw)
print(c)
fw.close()
print('end')

print('***'*4)
a = pickle.dumps(dataDic)
print(pickle.loads(a))
