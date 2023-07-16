#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User

all_classes = {'BaseModel': BaseModel, 'User': User,
               'Amenity': Amenity, 'City': City, 'State': State,
               'Place': Place, 'Review': Review}

class FileStorage():
    """
    Works as a storage engine.
    Serializes instances to a JSON file
    and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing
        """
        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as f:
            deserialized_obj = json.load(f)

            FileStorage.__objects = {
                k: all_classes[k.split('.')[0]](**v)
                for k, v in deserialized_obj.items()}
