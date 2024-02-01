#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship

from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        name = ""
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            from models import storage
            from models.city import City
            my_list = []
            # my_dict = storage.all('City')
            for value in storage.all(City).values():
                if self.id == value.state_id:
                    my_list.append(value)
            return my_list
        # def cities(self):
        #     """returns the list of City"""
        #     from models import storage
        #     from models.city import City

        #     result = []
        #     for value in storage.all(City).values():
        #         if value.state_id == self.id:
        #             result.append(value)
        #     return result
