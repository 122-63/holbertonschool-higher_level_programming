#!/usr/bin/python3
"""define a Base class"""
import json


class Base:
    """
    This class will be the base of
    all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """..."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list of dicts"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
