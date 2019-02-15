from flask_restful import Resource, reqparse, abort
from flask import jsonify
from src.models.todo import TodoModel, TodoSchema
from src.database import db


# api/v1/todos
class TodoListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', required=True)
        super(TodoListAPI, self).__init__()

    def get(self):
        todos = TodoModel.query.all()
        todos_data = TodoSchema(many=True).dump(todos).data
        return jsonify({'todos': todos_data})

    def post(self):
        args = self.reqparse.parse_args()
        todo = TodoModel(args.title)
        db.session.add(todo)
        db.session.commit()
        res = TodoSchema().dump(todo).data
        return res, 201


# api/v1/todos/<id>
class TodoAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title')
        super(TodoAPI, self).__init__()

    def get(self, id):
        todo = db.session.query(TodoModel).filter_by(id=id).first()
        if todo is None:
            abort(404)

        res = TodoSchema().dump(todo).data
        return res

    def put(self, id):
        todo = db.session.query(TodoModel).filter_by(id=id).first()
        if todo is None:
            abort(404)

        args = self.reqparse.parse_args()
        # Use code below for multiple params
        # for name, value in args.items():
        #   if value is not None:
        #     setattr(hoge, name, value)
        if args['title'] is not None:
            setattr(todo, 'title', args['title'])
        db.session.add(todo)
        db.session.commit()
        res = TodoSchema().dump(todo).data
        return res, 200

    def delete(self, id):
        todo = db.session.query(TodoModel).filter_by(id=id).first()
        if todo is None:
            db.session.delete(todo)
            db.session.commit()
        return None, 204
