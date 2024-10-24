from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class BaseModel:
    @classmethod
    def create(cls, **kwargs):
        raise NotImplementedError("Must be implemented in child classes.")

    @classmethod
    def get_by_id(cls, id):
        raise NotImplementedError("Must be implemented in child classes.")

    @classmethod
    def update(cls, id, **kwargs):
        raise NotImplementedError("Must be implemented in child classes.")

    @classmethod
    def delete(cls, id):
        raise NotImplementedError("Must be implemented in child classes.")

class User(BaseModel, SQLAlchemy):
    __tablename__ = 'users'

    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), default=None, nullable=True)
    last_name = db.Column(db.String(128), default=None, nullable=True)

    def __repr__(self):
        return f"User('{self.email}', '{self.first_name}', '{self.last_name}')"
