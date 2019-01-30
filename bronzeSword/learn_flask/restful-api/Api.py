#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):

	def get(self):
		return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
	app.run(debug = True)
'''


'''
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):

	def get(self, todo_id):
		return {todo_id: todos[todo_id]}

	def put(self, todo_id):
		todos[todo_id] = request.form['data']
		return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, "/<string:todo_id>")

if __name__ == "__main__":
	app.run(debug = True)
'''


#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
	'todo1': {'task': '学习计算机'},
	'todo2': {'task': '学习金融'},
	'todo3': {'task': '学习英语'}
}

def abort_if_todo_doesnt_exist(todo_id):
	if todo_id not in TODOS:
		abort(404, message = 'Todo {} doesn"t exist'.format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

class Todo(Resource):
	def get(self, todo_id):
		abort_if_todo_doesnt_exist(todo_id)
		return TODOS[todo_id]

	def delete(self, todo_id):
		abort_if_todo_doesnt_exist(todo_id)
		del TODOS[todo_id]
		return '', 204

	def put(self, todo_id):
		args = parser.parse_args()
		task = {'task': args['task']}
		TODOS[todo_id] = task
		return task, 201

class TodoList(Resource):
	def get(self):
		return TODOS

	def post(self):
		args = parser.parse_args()
		todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
		todo_id = 'todo%i' % todo_id
		TODOS[todo_id] = {'task': args['task']}
		return TODOS[todo_id], 201

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == "__main__":
	app.run(debug = True)


















