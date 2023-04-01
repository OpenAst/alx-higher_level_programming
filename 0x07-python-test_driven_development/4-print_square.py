#!/usr/bin/python3

"""
This is the "4-print_square" module.
The 4- print_square supplies one module , print_square(size)
"""

def print_square(size):
    """prints a square that has chareacter "#" with lenght of size.

    Args:
        size: represent size of the square

    Returns:
        no return

    Raises:
        TypeError: if size is not an int.
        ValueError: if size is less than zero.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(('#' * size + "\n") * size, end="")
