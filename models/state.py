#!/usr/bin/python3
""" State Module for HBNB project """

import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class """
    __tablename__ = "states"
    __table_args__ = (
        {'mysql_default_charset': 'latin1'})
    if models.storage_t == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            cities_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
