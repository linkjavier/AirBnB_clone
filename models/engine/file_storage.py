#!/usr/bin/python3
"""Class FileStorage """
import json
from models.base_model import BaseModel
from models.user import User

obj_class = {'BaseModel': BaseModel, 'User': User}


class FileStorage:
    """
        Serializes instances to a JSON file and deserializes
        JSON file to instances:
    """
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """ init method """
        pass

    def all(self):
        """
            Returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
            Sets in __objects the obj with
            key <obj class name>.id
        """

        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                              obj.id)] = obj

    def save(self):
        """ Save the object """

        dic = {}
        for key, value in FileStorage.__objects.items():
            dic.update({key: value.to_dict()})
        dic_dumps = json.dumps(dic)
        with open(FileStorage.__file_path, "w") as file:
            file.write(dic_dumps)

    def reload(self):
        """ Reload the object """

        try:
            with open(FileStorage.__file_path) as file:
                list_l = json.load(file)
            for key, value in list_l.items():
                key_class = key.split(".")
                FileStorage.__objects.update({key: obj_class[key_class[0]](**value)})
        except:
            pass
