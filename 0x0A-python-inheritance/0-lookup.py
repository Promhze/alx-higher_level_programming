#!/usr/bin/python3
""" Function that returns a lists of all items.
    in an object."""


def lookup(obj):
    """Returns list of attributes in an object."""
    return dir(obj)
