#!/usr/bin/python3
"""
This is User class to represent new users
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User subclass that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
