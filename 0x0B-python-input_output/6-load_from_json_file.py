#!/usr/bin/python3
"""Function creates an object from a JSON file"""


import json


def load_from_json_file(filename):
    """Performs deserialise from a json file"""

    with open(filename, 'r') as f:
        return json.load(f)
