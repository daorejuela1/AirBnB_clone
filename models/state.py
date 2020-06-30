#!/usr/bin/python3
"""
This is state class represents new states
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ State subclass that inherits from BaseModel """
    name = ""
