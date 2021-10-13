#!/usr/bin/python3
"""
task 9
"""


class Student:
    """empty class"""

    def __init__(self, first_name, last_name, age):
        """defines a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation of a Student"""
        return self.__dict__
