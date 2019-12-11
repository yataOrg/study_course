#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-12-03 11:25:26
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-12-03 11:44:03

from selenium import webdriver
import time

if __name__ == "__main__":
	driver = webdriver.Chrome()
	driver.get("https://baidu.com")
	print(driver.page_source)
	time.sleep(5)
	driver.close()