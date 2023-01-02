#!/usr/bin/python3

""" Print a square with a certain dimension, size"""


def print_square(size):

    """Print the square,
    Return type and value error is size
    less than zero and not an integer"""

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
