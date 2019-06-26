#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yata
# @Date:   2019-06-19 14:58:46
# @Last Modified by:   yata
# @Last Modified time: 2019-06-19 15:05:38

def get_data():

	return list(x ** 2 for x in (2, 4, 8))

print(get_data())