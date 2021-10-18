#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """new Rectangle"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """setter-getter the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """.width.setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """setter-getter the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """height.setter."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set-get the x cordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """x.setter."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set-get the y cordinate ofthe rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """..."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """print the rectangle using the # character"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        for y in range(self.y):
            print("")

        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """str"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
