#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yata
# @Date:   2019-07-17 10:00:38
# @Last Modified by:   yata
# @Last Modified time: 2019-07-17 10:21:43

import re

c = re.search("\d{17}[0-9Xx]", "ddfd41082X19901213007X")
print(c.group())