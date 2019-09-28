#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yata
# @Date:   2019-06-26 09:42:16
# @Last Modified by:   yata
# @Last Modified time: 2019-06-26 12:09:52

import os

def osPath():

	path = os.path.dirname(__file__)
	print(path)

	basename = os.path.basename(__file__)
	print(basename)
	print(__file__)

	is_have = os.path.exists(__file__)
	print(is_have)

	file_size = os.path.getsize(__file__)
	print(file_size)

	is_mount = os.path.ismount(__file__)
	print(is_mount)

	file_normcase = os.path.normcase(__file__)
	print(file_normcase)

	file_split = os.path.split(__file__)
	print(file_split)

	file_splitdrive = os.path.splitdrive(__file__)
	print(file_splitdrive)

# osPath()

def os_walk():

	if False == os.path.isdir(os.path.dirname(__file__)):
		print("not a true dir")
		return

	print(os.path.dirname(__file__))
	for dir_path, subpaths, files in os.walk("/usr/local/etc/", False):
		print(dir_path, subpaths, files)


# print(os_walk())




