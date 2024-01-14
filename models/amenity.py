#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref

if environ.get('HBNB_TYPE_STORAGE') == 'db':

    class Amenity(BaseModel, Base):
        """Class Amenity for DB"""
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place',
                                       secondary='place_amenity',
                                       back_populates='amenities')
else:
    class Amenity(BaseModel):
        """Class Amenity for FS"""

        name = ''
