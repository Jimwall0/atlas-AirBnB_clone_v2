#!/usr/bin/python3
"""BaseModel module with SQLAlchemy support"""

from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
import uuid

# SQLAlchemy Base class
Base = declarative_base()

class BaseModel:
    """A base class for all models with SQLAlchemy support"""

    # SQLAlchemy Columns
    id = Column(String(60), primary_key=True, nullable=False, default=str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model using kwargs"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.utcnow()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self):
        """Updates updated_at with current time and saves the instance"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)  # Add to storage
        models.storage.save()  # Commit to storage

    def to_dict(self):
        """Converts instance into a dictionary format, excluding SQLAlchemy state"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]  # Remove SQLAlchemy state info
        return dictionary

    def delete(self):
        """Deletes the current instance from storage"""
        models.storage.delete(self)
