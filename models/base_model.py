#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for kw, value in kwargs.items():
                if kw == "created_at" or kw == "updated_at":
                    self.__dict__[kw] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[kw] = value
        else:
           models.storage.new(self)

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()
    
    def to_dict(self):
        """Returns a dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        copyDict = self.__dict__.copy()
        copyDict["created_at"] = self.created_at.iosformat()
        copyDict["updated_at"] = self.updated_at.isoformat()
        copyDict["__class__"] = self.__class__.__name__
        return copyDict
    
    def __str__(self):
        """Return the str representation of the BaseModel instance."""

        className = self.__class__.__name__
        return f"[{className}] ({self.id}) {self.__dict__}"