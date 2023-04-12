#!/usr/bin/python3
"""A module that creates a class student"""


class Student():
    """a class that defines student"""


    def __init__(self, first_name, last_name, age):
        """initialization of Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of Student"""
        return self.__dict__
