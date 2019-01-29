#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
def app(environ, start_response):
	data = b"Hello, World!\n"
	start_response("200 OK", [
			("Content-Type", "text/plain"),
			("Content-Length", str(len(data)))
	])
	return iter([data])
'''

'''
def app(environ, start_response):
	data = b"Hello, World!\n"
	status = "200 OK"
	response_headers = [
		("Content-Type": "text/plain"),
		("Content-Length": str(len(data)))
	];
	start_response(status, response_headers)
	return iter([data])
'''

# werkzeug
from werkzeug.wrappers import Request, Response

@Request.application
def hello(request):
	return Response("hello world")

if __name__ == "__main__":
	from werkzeug.serving import run_simple
	run_simple("localhost", 4000, hello)