#!/usr/bin/python3
"""This module defines a FileStorage class"""
import json
import datetime


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets obj in __objects with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        def datetime_converter(x):
            if isinstance(x, datetime.datetime):
                return x.__str__()

        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_dict, f, default=datetime_converter)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.load(f)
            for key, value in json_dict.items():
                cls_name = value["_class_"]
                cls = eval(cls_name)
                FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass