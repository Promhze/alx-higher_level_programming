#!/usr/bin/python3

"""Define a Square class"""


class Square:

    """Represents the square"""

    def __init__(self, size=0):

        """Initialize the size"""

        self.size = size

    @property
    def size(self):
        """Get size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Define the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print to stdout with #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
