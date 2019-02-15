from flask import Flask, jsonify
from flask_restful import Api
from src.database import init_db
from src.apis.todos import TodoListAPI, TodoAPI


def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')
    init_db(app)

    api = Api(app)
    api.add_resource(TodoListAPI, '/api/v1/todos')
    api.add_resource(TodoAPI, '/api/v1/todos/<id>')

    return app


app = create_app()
