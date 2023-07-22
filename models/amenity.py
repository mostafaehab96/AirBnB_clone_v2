#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Definition of class Amenity."""
    from models import storage_t
    __tablename__ = "amenities"
    __table_args__ = (
        {'mysql_default_charset': 'latin1'})
    if storage_t == "db":
        from models.place import place_amenity
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity,
                                       back_populates="amenities")
    else:
        name = ""
