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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list of dicts"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """create new file with Json"""
        filename = cls.__name__+'.json'
        list = []
        if list_objs is not None:
            for i in list_objs:
                list.append(cls.to_dictionary(i))

        with open(filename, 'w') as jfile:
            jfile.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
