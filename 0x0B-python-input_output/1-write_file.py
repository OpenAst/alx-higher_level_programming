#!/usr/bin/python3
"""This module defines a text file writing function"""


def write_file(filename="", text=""):
    """returns the number of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
