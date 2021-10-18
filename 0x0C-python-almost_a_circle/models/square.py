#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """new square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """set-get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """size.setter."""
        self.width = value
        self.height = value

    def __str__(self):
        """str"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)
