#!/usr/bin/python3
""" a module that create a class Square"""

class Square:
    """a classs that represent a squar
    Initialising this class
    Args: size - represent the size of the square
    Raises:
    TypeError- if size if not an integer
    ValueError- if size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    self.__size = size
    
    @property
    def size(self):
        """Retrieves the size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """set a new value to the size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    
    def area(self):
        """returns the area of a square"""
        return(self._size ** 2)
