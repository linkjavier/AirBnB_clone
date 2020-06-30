#!/usr/bin/python3
""" Class Model Module """
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Defines all common attributes/methods """

    def __init__(self, *args, **kwargs):
        """Init Basemodel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value_2 = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value_2)
                elif not key == '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
            Prints: [<class name>] (<self.id>) <self.__dict__>
        """
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__))

    def save(self):
        """
            Updates the public instance attribute updated_at
            with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        dict = self.__dict__.copy()
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        dict['__class__'] = self.__class__.__name__
        return dict
