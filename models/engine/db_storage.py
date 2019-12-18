#!/usr/bin/python3
"""This is the db_storage.py File dbStorage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker
import inspect
from sqlalchemy import (create_engine)
from sqlalchemy import select

import os
import sys


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __engine: path to the JSON file
        __session: objects will be stored
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of base model class"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(os.environ["HBNB_MYSQL_USER"],
                                                 os.environ["HBNB_MYSQL_PWD"],
                                                 os.environ["HBNB_MYSQL_HOST"],
                                                 os.environ["HBNB_MYSQL_DB"]),
            pool_pre_ping=True)
        if os.environ["HBNB_ENV"] == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method all of dbStorage class"""
        my_cls = ["State", "City", "User", "Amenity", "Place", "Review"]
        my_dict = {}
        if cls is None:
            for table in my_cls:
                query = self.__session.query(eval(table)).all()
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    # other = (obj.__dict__)
                    # del other["_sa_instance_state"]
                    # new = dict(other)
                    # my_dict[key] = new
                    my_dict[key] = obj
                # print(my_dict)
            return my_dict
        else:
            print("No None")
            # query = self.__session.query(eval(cls)).all()
            query = self.__session.query(eval(cls)).all()
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                my_dict[key] = obj
            # print(my_dict)
                return my_dict

    def new(self, obj):
        """Method new of dbStorage class"""
        if obj:
            mod_obj = obj
            self.__session.add(mod_obj)

    def save(self):
        """Method save of dbStorage class"""
        my_dict = {}
        # for key, value in self.__dict__.items():
        # my_dict[key] = value.to_dict()
        # self.__session.add(my_dict)
        self.__session.commit()

    def delete(self, obj=None):
        """Method save of dbStorage class"""
        if obj:
            result = self.__session.query(eval(obj)).\
                filter(id == obj.id).first()

            result.delete()

    def reload(self):
        """Method reload of dbStorage class"""

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker()
        Session.configure(bind=self.__engine)
        self.__session = Session()
