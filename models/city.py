#!/usr/bin/python3
""" City Class """
from models.base_model import BaseModel
from models.base_model import State


class City(BaseModel):
    """
        Class City that inherits from BaseModel
    """
    state_id = ""
    name = ""
