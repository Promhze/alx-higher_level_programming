#!/usr/bin/python3
"""Function that performs deserializing"""


import json


def from_json_string(my_str):
    """Converts a json string to a python data object
    Deseializing"""

    return json.loads(my_str)
