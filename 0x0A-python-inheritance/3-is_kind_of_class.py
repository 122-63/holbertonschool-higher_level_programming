#!/usr/bin/python3
"""return True or False"""


def is_kind_of_class(obj, a_class):
    """return True or False"""
    if isinstance(obj, a_class):
        return True
    return False
