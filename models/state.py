#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from os import environ
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


if environ.get('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class for DB"""
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='states', cascade='all, delete')

else:
    class State(BaseModel):
        """State class for FS"""
        name = ''

        @property
        def cities(self):
            """Returns the list of City instances"""
            from models import storage
            return[city
                   for city in storage.all(City).values()
                   if city.state_id == self.id]
