#!/usr/bin/python3
"""Class FileStorage """
import json
from models.base_model import BaseModel


class FileStorage:
    """
        Serializes instances to a JSON file and deserializes
        JSON file to instances:
    """
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """ init"""
        pass
    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects
    def new(self, obj):
        """ sets in __objects the obj with
             key <obj class name>.id
        """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    def save(self):
        """Save"""
        dic = {}
        for key, value in FileStorage.__objects.items():
            dic.update({key: value.to_dict()})
        dic_dumps = json.dumps(dic)
        with open(FileStorage.__file_path, "w") as file:
            file.write(dic_dumps)

    def reload(self):
        """Reload"""

        try:
            with open(FileStorage.__file_path) as file:
                list_l = json.load(file)
            for key, value in list_l.items():
                FileStorage.__objects[key] = BaseModel(**value)
        except:
            pass
