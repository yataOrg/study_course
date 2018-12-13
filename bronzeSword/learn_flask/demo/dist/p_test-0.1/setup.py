#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from setuptools import setup

setup(
    name='p_test',
    version='0.1',
    py_modules=['demo_click'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        demo_click=demo_click:hello
    ''',
)
