#!/usr/bin/python3
""" Class Model Module """
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ Defines all common attributes/methods """

    def __init__(self):
        """Init"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
            Prints: [<class name>] (<self.id>) <self.__dict__>
        """
        print("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
            Updates the public instance attribute updated_at
            with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        dict  = self.__dict__.copy()




