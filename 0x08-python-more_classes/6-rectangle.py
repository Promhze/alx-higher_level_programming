#!/usr/bin/python3
"""A simple triangle class"""


class Rectangle:
    """Defines the width and height"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialise the size of the rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """Print the rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rect += '#'
            rect += '\n'
        return rect[:-1]

    def __repr__(self):
        """Represents the rectangle using eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Detects when a rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
