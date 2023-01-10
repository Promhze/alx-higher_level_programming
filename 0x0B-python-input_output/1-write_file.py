#!/usr/bin/python3
"""Function that writes a string to a file"""


def write_file(filename="", text=""):
    """Function puts text in the filename"""

    with open(filename, 'w+') as f:
        my_write = f.write(text)
        return my_write
