#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time


def show_time(func):
    print(time.ctime())
    return func()

@show_time
def abc():
    print("hello world %s %s" % ("yanzhipeng", "limihu"))


if __name__ == "__main__":
    abc