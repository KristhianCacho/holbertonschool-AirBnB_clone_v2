#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref='state', cascade="all, delete")

    @property
    def cities(self):
        """ Getter for cities """
        l = []
        dic = models.storage.all(City)
        for city in dic.values():
            if city.state_id == self.id:
                l.append(city)
        return l
