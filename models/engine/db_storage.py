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
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.environ["HBNB_MYSQL_USER"], os.environ["HBNB_MYSQL_PWD"],
                                      os.environ["HBNB_MYSQL_HOST"], os.environ["HBNB_MYSQL_DB"]),
                                      pool_pre_ping=True)
        if os.environ["HBNB_ENV"] == "test":
            Base.metadata.drop_all(self.__engine)
            #tables = self.__session.query('*').all()

            #for table in tables:
             #   table.delete()

            #self.__session.commit()

    def all(self, cls=None):
        """Method all of dbStorage class"""
        my_cls = ["State", "City"]
        my_dict = {}
        if cls is None:
            #tbl = Base.metadata.tables.keys()
            for table in my_cls:
                query = self.__session.query(eval(table)).all()
                for element in query:
                    key = eval(table) + '.' + element.id
                    my_dict[key] = element
                print(my_dict)
                return my_dict
        else:
            print("No None")
            #query = self.__session.query(eval(cls)).all()
            query = self.__session.query(eval(cls)).all()
            for element in query:
                key = eval(cls) + '.' + element.id
                my_dict[key] = element
            return my_dict

    def new(self, obj):
        """Method new of dbStorage class"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Method save of dbStorage class"""
        my_dict = {}
        #for key, value in self.__dict__.items():
         #   my_dict[key] = value.to_dict()
        #self.__session.add(my_dict)
        self.__session.commit()

    def delete(self, obj=None):
        """Method save of dbStorage class"""
        if obj:
            result = self.__session.query(eval(obj)).filter(id == obj.id).first()

            result.delete()

    def reload(self):
        """Method reload of dbStorage class"""
        try:
            Base.metadata.create_all(self.__engine)
            Session = sessionmaker()
            Session.configure(bind=self.__engine)
            self.__session = Session()
            query = select('*').select_from(State).order_by(State.id)
            data = self.__session.execute(query).fetchall()
            for row in data:
                print('{}: {}'.format(row.id, row.name))
        except:
            pass
