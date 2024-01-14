#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from os import environ
from sqlalchemy.orm import relationship, backref
from models.place import Place


if environ.get('HBNB_TYPE_STORAGE') == 'db':

    class User(BaseModel, Base):
        """This class defines a user by various attributes DB"""
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user",
                              cascade='all, delete')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete')
else:
    class User(BaseModel):
        """This class defines a usar by various attributes FS"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''
