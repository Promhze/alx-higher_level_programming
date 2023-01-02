#!/usr/bin/python3
"""A simple triangle class"""


class Rectangle:
    """Defines the width and height"""

    def __init__(self, width=0, height=0):
        """Initialise the size of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Gives the width a value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Gives the height a value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Checks the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
