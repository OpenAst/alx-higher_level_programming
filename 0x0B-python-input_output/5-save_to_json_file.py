#!/usr/bin/python3
"""This module rites a JSON representation of a file to a text file"""

import json

def save_to_json_file(my_obj, filename):
    """writes a JSON string to a text file"""
    with open(filename, 'w', encoidng="utf-8") as f:
        json.dump(my_obj, f)
