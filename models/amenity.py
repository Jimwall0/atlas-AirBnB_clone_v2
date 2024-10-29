#!/usr/bin/python3
"""Amenity Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Represents an amenity for a place"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    def some_method_requiring_place_amenity(self):
        from models.place import place_amenity  # Import here to avoid circular dependency
