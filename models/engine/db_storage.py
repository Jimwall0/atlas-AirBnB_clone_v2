#!/usr/bin/python3
"""Defines the DBStorage engine."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """Manages storage for database."""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database storage engine"""
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        HBNB_ENV = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects in the database"""
        pass

    def new(self, obj):
        """Add the object to the current database session"""
        pass

    def save(self):
        """Commit all changes of the current database session"""
        pass

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        pass

    def reload(self):
        """Reloads data from the database"""
        pass
