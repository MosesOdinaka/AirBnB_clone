#!/usr/bin/python3
"""This module defines the BaseModel class"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes and methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the BaseModel class"""
        self.my_number = 0
        self.name = None
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime
                    (value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime
                    (value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        d = {
            "id": self.id,
            "created_at": self.created_at,
            "my_number": self.my_number,
            "updated_at": self.updated_at,
            "name": self.name
        }
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, d)

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        d = {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "__class__": self.__class__.__name__,
            "my_number": self.my_number,
            "updated_at": self.updated_at.isoformat(),
            "name": self.name
        }
        return d