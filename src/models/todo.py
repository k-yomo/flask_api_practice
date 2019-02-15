from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy_utils import UUIDType
from src.database import db

import uuid

ma = Marshmallow()


class TodoModel(db.Model):
    __tablename__ = 'todos'

    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<TodoModel {}:{}>'.format(self.id, self.title)


class TodoSchema(ma.ModelSchema):
    class Meta:
        model = TodoModel

    created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    updated_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
