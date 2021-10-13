#!/usr/bin/python3
"""
task 8 : Class to JSON
"""


def class_to_json(obj):
    """eturns the dictionary description with simple data structure"""
    return obj.__dict__
