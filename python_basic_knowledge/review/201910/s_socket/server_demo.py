#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-09 15:29:11
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-09 16:02:28

import socket

s = socket.socket()
host = socket.gethostname()
port = 22345

s.bind((host, port))

s.listen(5)

while True:
	c, addr = s.accept()
	print("连接地址-",  addr)
	c.send("你好小哆哆!".encode('utf-8'))
	c.close()
	break

