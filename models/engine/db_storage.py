#!/usr/bin/python3
"""This module defines a class to manage DB Storage for hbnb clone"""
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
import sqlalchemy as db

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """This class manages storage of hbnb models in a database"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor for DBStorage class"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'. format(
                HBNB_MYSQL_USER,
                HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST,
                HBNB_MYSQL_DB),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        # my_dict = {}
        # if cls is None:
        #     for obj in classes:
        #         table = self.__session.query(classes[obj]).all()
        #         for obj in table:
        #             key = f"{obj.__class__.__name__}.{obj.id}"
        #             my_dict[key] = obj
        #     return my_dict
        # else:
        #     table = self.__session.query(cls).all()
        # for obj in table:
        #     key = f"{obj.__class__.__name__}.{obj.id}"
        #     my_dict[key] = obj
        # return my_dict
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is None:
            return
        self.__session.delete(obj)

    def reload(self):
        """reload method"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """hello"""
        self.__session.close()

    def get(self, cls, id):
        """A method to retrieve one object or None from the current database"""
        if cls not in classes.values():
            return None
        return self.__session.query(cls).filter(cls.id == id).first()

    def count(self, cls=None):
        """method to count the number of objects in storage"""
        return len(self.all(cls))
