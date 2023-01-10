#!/usr/bin/python3
"""Function handles Serializing"""


import json


def to_json_string(my_obj):
    """converts a python object to a json string
    Seializing"""

    return json.dumps(my_obj)
