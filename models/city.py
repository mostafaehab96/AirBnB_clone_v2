#!/usr/bin/python
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Representation of city """
    __tablename__ = "cities"
    __table_args__ = (
        {'mysql_default_charset': 'latin1'})
    if models.storage_t == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", cascade="all, delete", backref="cities")
    else:
        state_id = ""
        name = ""
