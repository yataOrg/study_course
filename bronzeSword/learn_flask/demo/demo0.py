#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
export FLASK_APP=demo0.py
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run
flask run --host=0.0.0.0
"""

from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return 'this is index page'


@app.route("/hello")
def hello():
    return 'this is hello page'


@app.route("/id/<int:user_id>")
def get_user(user_id):
    return "this is user_id is {}".format(user_id)


@app.route("/name/<user_name>")
def get_name(user_name):
    return "this user_name is {0}".format(user_name)


@app.route("/path/<path:subpath>")
def get_path(subpath):
    return "this subpath is {}".format(subpath)


@app.route("/float/<float:float>")
def get_float(float):
    return "this float is {}".format(float)


with app.test_request_context():
    print(url_for('hello'))
    print(url_for('get_user', user_id='343434'))
    print(url_for('get_name', user_name='ppker'))
    print(url_for('get_path', subpath='dsafsadf/dsfdsafds'))