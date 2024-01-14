#!/usr/bin/python3
"""DBStorage Module"""

from os import environ
from models.base_model import Base, BaseModel
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"City": City, "State": State, "User": User,
           "Place": Place, "Review": Review, "Amenity": Amenity}


class DBStorage:
    """DBStorage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new instance of the DBStorage class."""
        user = environ.get('HBNB_MYSQL_USER')
        password = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST')
        database = environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host,
                                             database), pool_pre_ping=True)

        if environ.get('HBNB_ENV') == 'test':
            Base.metada.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls).
        """
        obj_dict = {}

        if cls:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[key] = obj
        else:
            for cls in classes:
                objects = self.__session.querry(cls).all()
                for obj in objects:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Adds the object to the current database session (self.__session)."""
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current
        database session (self.__session).
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session obj if not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and create
        the current database session.
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()

    def close(self):
        """discard the Session itself"""
        if self.__session:
            self.__session.close()
