#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-09 15:38:10
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-09 16:01:18

import socket

s = socket.socket()
host = socket.gethostname()
port = 22345

s.connect((host, port))

data = s.recv(1024)
print(data.decode('utf-8'))
s.close()



