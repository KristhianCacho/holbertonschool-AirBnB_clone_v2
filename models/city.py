#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from os import environ
from sqlalchemy.orm import relationship, backref
from models.place import Place


if environ.get('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="city",
                              cascade="all, delete")

else:
    class City(BaseModel):
        """ The city class, contains state ID and name """
        name = ''
        state_id = ''
