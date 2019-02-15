from flask import Flask, jsonify
from flask_restful import Api
from src.database import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')
    init_db(app)

    api = Api(app)

    return app


app = create_app()
