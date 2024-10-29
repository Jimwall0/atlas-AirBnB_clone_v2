#!/usr/bin/python3
"""Place Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

# Define the association table `place_amenity`
place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', ForeignKey('amenities.id'), primary_key=True)
)

class Place(BaseModel, Base):
    """Represents a place for a MySQL database"""
    __tablename__ = 'places'
    name = Column(String(128), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
