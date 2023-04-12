#!/usr/bin/python3
"""This module prints a json representation of an object"""

import json

def to_json_string(my_obj):
    """returns the JSON representation of an object string"""
    return json.dumps(my_obj)
