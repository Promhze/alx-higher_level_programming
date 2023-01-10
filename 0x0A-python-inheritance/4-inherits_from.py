#!/usr/bin/python3
"""Function that return True if the object is an instance of a class
that inherited (directly or indirectly)"""


def inherits_from(obj, a_class):
    """Checks instance of a class.

    Args:
        -obj: object to check instance
        -a_class: class to check it to
        """

    return isinstance(obj, a_class) and type(obj) != a_class
