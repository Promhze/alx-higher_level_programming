#!/usr/bin/python3
"""Create a new class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle.
    Private instance attributes:
        - width
        - height
    Inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Initializes an instance.
        Args:
            - width: width of the rectangle
            - heigth: height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a string format."""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Computes the area of the rectangle"""

        return self.__width * self.__height
