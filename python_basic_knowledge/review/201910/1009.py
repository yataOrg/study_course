#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-08 12:03:04
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-08 14:54:04

import MySQLdb

db = MySQLdb.connect('localhost', 'root', '123456', 'getyii', charset='utf8')

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version is %s" % (data, ))
db.close()


