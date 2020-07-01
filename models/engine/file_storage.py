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
        class_name = type(obj).__name__
        my_id = obj.id
        instance_key = class_name + "." + my_id
        FileStorage.__objects[instance_key] = obj

    def save(self):
        """ saves in json format to a file """
        my_obj_dict = {}
        for key in FileStorage.__objects:
            my_obj_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as file_path:
            json.dump(my_obj_dict, file_path)

    def reload(self):
        """ loads from json file """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        my_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as file_path:
            objects = json.load(file_path)
            FileStorage.__objects = {}
            for key in objects:
                name = key.split(".")[0]
                FileStorage.__objects[key] = my_dict[name](**objects[key])
