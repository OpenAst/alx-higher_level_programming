#!/usr/bin/python3
"""a module that defines a rectangle"""

class Rectangle():
    """class with a private attribute"""
    def __init__(self, width=0, height=0):
        """initiation of class Rectangle
        Args:
            width: 0
            height: 0
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Getter for attribute width"""
            return self.__width

        @width.setter
        def width(self,value):
            """Setter for attribute width"""
            if type(value) is not int:
                raise TypeError("width must be an integer")

            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """Getter for attribute height"""
            return self.__height

        @height.setter
        def height(self, value):
            """Setter for attribute height"""
            if type(value) is not int:
                raise TypeError('height must be an integer')

            if value < 0:
                raise ValueError('height must be >= 0')

            self.__height = value
