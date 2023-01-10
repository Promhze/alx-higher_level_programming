#!/usr/bin/python3
"""A function that reads a file"""


def read_file(filename=""):
    """Use the with statement to read a file"""

    with open(filename) as f:
        my_read = f.read()
        print(my_read, end="")
