#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from os import environ
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             nullable=False)
                      )

if environ.get('HBNB_TYPE_STORAGE') == 'db':

    class Place(BaseModel, Base):
        """ A place to stay DB"""
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
        amenities = relationship("Amenity",
                                 secondary='place_amenity',
                                 back_populates='place_amenities',
                                 viewonly=False)

else:
    class Place(BaseModel):
        """A place to stay FS"""
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = ''
        number_bathrooms = ''
        max_guest = ''
        price_by_night = ''
        latitude = ''
        longitude = ''
        amenity_ids = []

        @property
        def reviews(self):
            """ FileStorage relationship between Place and Review """
            all_reviews = models.storage.all(Review)
            total_reviews = []
            for every_review in all_reviews.values():
                total_reviews.append(every_review)
            return (total_reviews)

        @property
        def amenities(self):
            """Getter for amenity.id linked to Place class"""
            self.amenity_ids = models.storage.all(Amenity)
            return (self.amenity_ids)

        @amenities.setter
        def amenities(self, id):
            """
            handles append method for adding an
            Amenity.id to the attribute amenity_ids
            """
            if id.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(id)
