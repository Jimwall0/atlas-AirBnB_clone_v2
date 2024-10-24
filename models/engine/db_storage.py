#!/usr/bin/python3
"""DBStorage class definition"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os

class DBStorage:
    """Database storage engine using SQLAlchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database connection"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{db}', pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query the current database session"""
        result = {}
        if cls:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = f'{type(obj).__name__}.{obj.id}'
                result[key] = obj
        else:
            # Query all classes
            for class_name in [State, City]:
                query_result = self.__session.query(class_name).all()
                for obj in query_result:
                    key = f'{type(obj).__name__}.{obj.id}'
                    result[key] = obj
        return result

    def new(self, obj):
        """Add object to the current session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the current session if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and initialize the session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
