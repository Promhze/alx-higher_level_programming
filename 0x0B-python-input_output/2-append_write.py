#!/usr/bin/python3
"""Function appends a string to a file."""


def append_write(filename="", text=""):
    """Adds a string to the end of a file.

    Args:
        filename - file to be added
        text - string to be appended

    Return: The number of characters added."""

    with open(filename, 'a+') as f:
        return f.write(text)
