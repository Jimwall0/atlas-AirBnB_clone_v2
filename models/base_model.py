#!/usr/bin/python3
"""BaseModel module defines common attributes for other classes."""

from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
import models

Base = declarative_base()  # Define the base for SQLAlchemy

class BaseModel:
    """Defines the BaseModel class with common attributes for other models."""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize new instance of BaseModel."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if self.created_at is None:
                self.created_at = datetime.utcnow()
            if self.updated_at is None:
                self.updated_at = datetime.utcnow()


    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {{'name': '{self.name}'}}"

    def save(self):
        """Save method for BaseModel."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Delete the current instance from storage."""
        models.storage.delete(self)

    def to_dict(self):
        """Convert instance to dictionary."""
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result.pop('_sa_instance_state', None)
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
