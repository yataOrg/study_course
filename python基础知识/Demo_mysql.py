#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import pymysql, time

# 打开数据库连接
db = pymysql.connect(host='140.143.32.44', user='root', password='yata123', db='yata_data_01', port=3306)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("show tables")

data = cursor.fetchall()

print(data)

a = '2018-11-14'
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")