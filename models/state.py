#!/usr/bin/python3
"""State module for the HBNB project."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """State class for handling state information."""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """Getter attribute cities that returns list of City instances with state_id equal to current State.id"""
        from models import storage
        from models.city import City
        return [city for city in storage.all(City).values() if city.state_id == self.id]
