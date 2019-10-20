#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-10-16 21:56:19
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-10-17 13:23:23

import requests

r = requests.get("https://api.github.com/user", auth=('user', 'pass'))
print(r)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print("***" * 3)
print(r.json)