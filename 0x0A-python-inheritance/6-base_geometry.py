#!/usr/bin/python3
"""A base geometry class."""


class BaseGeometry:
    """Class with public instance method."""

    def area(self):
        """method that raises an exception."""

        raise Exception("area() is not implemented")
