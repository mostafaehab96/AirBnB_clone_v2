#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import uuid
from datetime import datetime
import models
from os import getenv
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(),
                        nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(),
                        nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs.get("__class__"):
            kwargs.pop("__class__")

        if kwargs.get("created_at"):
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])

        if kwargs.get("updated_at"):
            kwargs["updated_at"] = datetime.fromisoformat(kwargs["updated_at"])

        self.__dict__.update(kwargs)

    def __str__(self):
        """Returns string representation of the class."""
        name = self.__class__.__name__
        dic = self.__dict__.copy()
        if "_sa_instance_state" in dic:
            del dic["_sa_instance_state"]
        return f"[{name}] ({self.id}) {dic}"

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        cls_dict = self.__dict__.copy()
        cls_dict["__class__"] = self.__class__.__name__
        cls_dict["created_at"] = self.created_at.isoformat()
        cls_dict["updated_at"] = self.updated_at.isoformat()

        if "_sa_instance_state" in cls_dict:
            del cls_dict["_sa_instance_state"]

        return cls_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
