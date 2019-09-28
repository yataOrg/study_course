#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yata
# @Date:   2019-07-03 00:04:54
# @Last Modified by:   yata
# @Last Modified time: 2019-07-05 19:52:19

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def test():

    test = sys.version_info
    print(test)

test()



class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

        Student(xiao_ming', 59)