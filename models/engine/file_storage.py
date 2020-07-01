#!/usr/bin/python3
"""
This engine is in charge of serial/unserial objects to files
"""
import json
import os


class FileStorage():
    """Serialize/Deserialize python data """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionaries """
        return (self.__objects)

    def new(self, obj):
        """ create a new object """
        class_name = type(obj).__name__
        my_id = obj.id
        instance_key = class_name + "." + my_id
        self.__objects[instance_key] = obj.to_dict()

    def save(self):
        """ saves in json format to a file """
        with open(FileStorage.__file_path, 'w') as file_path:
            file_path.write(json.dumps(self.__objects))

    def reload(self):
        """ loads from json file """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as file_path:
            my_data = file_path.read()
            if (my_data):
                self.__objects = json.loads(my_data)
