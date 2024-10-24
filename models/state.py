#!/usr/bin/python3
"""State class definition with SQLAlchemy support"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models

class State(BaseModel, Base):
    """State class that inherits from BaseModel and Base"""
    __tablename__ = 'states'

    # Name of the state (cannot be null)
    name = Column(String(128), nullable=False)

    # Relationship to cities (for DBStorage)
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """Getter for FileStorage: returns list of City instances linked to this State"""
        city_list = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
