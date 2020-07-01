#!/usr/bin/python3
"""
This engine is in charge of serial/unserial objects to files
"""
import json
import os


class FileStorage():
    """Serialize/Deserialize python data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionaries"""
        return (FileStorage.__objects)

    def new(self, obj):
        """ create a new object """
        if obj:
            class_name = obj.__class__.__name__
            my_id = obj.id
            instance_key = class_name + "." + my_id
            FileStorage.__objects[instance_key] = obj.to_dict()

    def save(self):
        """ saves in json format to a file """
        if FileStorage.__file_path:
            with open(FileStorage.__file_path, 'w') as file_path:
                json.dump(FileStorage.__objects, file_path)

    def reload(self):
        """ loads from json file """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as file_path:
            my_data = file_path.read()
            if (my_data):
                FileStorage.__objects = json.loads(my_data)
