#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import models
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    __table_args__ = (
        {'mysql_default_charset': 'latin1'})
    if models.storage_t == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", cascade="all, delete", backref="user")
        reviews = relationship("Review", cascade="all, delete", backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
