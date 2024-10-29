#!/usr/bin/python3
"""DBStorage engine for handling database interactions."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
import os

class DBStorage:
    """Database storage engine."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage instance."""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{db}', 
            pool_pre_ping=True
        )

        # Drop all tables if environment is 'test'
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all objects by class name."""
        obj_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
        else:
            # Add other model classes as needed for querying all
            objs = self.__session.query(State).all() + self.__session.query(City).all()
        for obj in objs:
            key = f"{obj.__class__.__name__}.{obj.id}"
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add object to current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create tables and initialize session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the current scoped session."""
        self.__session.remove()  # Optional for session cleanup

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
