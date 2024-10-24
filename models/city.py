#!/usr/bin/python3
"""City class definition with SQLAlchemy support"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """City class that inherits from BaseModel and Base"""
    __tablename__ = 'cities'

    # Name of the city (cannot be null)
    name = Column(String(128), nullable=False)

    # Foreign key linking to the state's ID
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
