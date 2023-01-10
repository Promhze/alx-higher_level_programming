#!/usr/bin/python3
"""Function serialise and saves to a file"""


import json


def save_to_json_file(my_obj, filename):
    """Converts a python object to json string
    and saves in a file.

    Args:
        -my_obj: Object to be serialized
        -filename: File to save json string
        """
    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
