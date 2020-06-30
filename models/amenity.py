#!/usr/bin/python3
"""
This is amenity class that represents new amenities
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity subclass that inherits from BaseModel """
    name = ""
