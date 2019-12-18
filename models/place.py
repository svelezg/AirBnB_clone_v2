#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('place.id')),
                      Column('amenity_id', String(60), ForeignKey('amenity.id'))
)


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    id = Column(String(60), nullable=False, primary_key=True)

    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        back_populates="amenities", viewonly=False)

    if os.environ['HBNB_TYPE_STORAGE'] != 'db':
            @property
            def amenities(self):
                """FileStorage relationship between Place and Amenity
                """
                places = storage.all(Place)
                places_relation = []
                for place in places.values():
                    if place.amenity_id == self.id:
                        places_relation = places_relation.append(place)
                return places_relation