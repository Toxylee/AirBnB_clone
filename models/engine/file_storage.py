#!/usr/bin/python3
""" defines a class called filestorage """
import json
from models.base_model import BaseModel


class FileStorage:
    """ serializes instance to JSON and vice versa """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets __objects the object with key <obj class name>.id """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to JSON file(path: __file_path) """
        copy = FileStorage.__objects
        obj_dict = {obj: copy[obj].to_dict() for obj in copy.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ deserializes JSON file only if __file_path exists """
        try:
            with open(FileStorage.__file_path) as f:
                objs = json.load(f)
                for object in objs.values():
                    name = object['__class__']
                    del object['__class__']
                    self.new(eval(name)(**object))
        except FileNotFoundError:
            return
