#!/usr/bin/python3
"""..."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('8-rectangle').Rectangle


class Rectangle(BaseGeometry):
    """..."""
    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """..."""
