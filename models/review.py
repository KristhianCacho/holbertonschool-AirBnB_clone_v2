#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import environ


if environ.get('HBNB_TYPE_STORAGE') == 'db':

    class Review(BaseModel, Base):
        """Review class to store review information DB"""
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
else:
    class Review(BaseModel):
        """ Review class to store review information FS"""
        place_id = ""
        user_id = ""
        text = ""
