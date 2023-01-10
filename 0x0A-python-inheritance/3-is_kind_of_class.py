#!/usr/bin/python3
""" Function that defines the instance of a class."""


def is_kind_of_class(obj, a_class):
    """Checks the instance of an object to a class.
    or if they are both same.

    Args:
        -obj: object to check the instance
        -a_class: Class to check it to.
        """
    if isinstance(obj, a_class):
        return True
    else:
        return False
