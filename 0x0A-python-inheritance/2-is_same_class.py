#!/usr/bin/python3
""" Function that defines the instance of a class."""


def is_same_class(obj, a_class):
    """Checks the instance of an object to a class.
    or if they are both same.

    Args:
        -obj: object to check the instance
        -a_class: Class to check it to.
        """

    return True if type(obj) is a_class else False
