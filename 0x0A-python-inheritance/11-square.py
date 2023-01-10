#!/usr/bin/python3
""" A multiple inherited class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is a multiple inherited square class"""

    def __init__(self, size):
        """Initialize the square method."""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Implement the area"""
        return self.__size ** 2
