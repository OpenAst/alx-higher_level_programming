#!/usr/bin/python3
"""
Algorithm for the max of a lsit of integer
"""

def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if list_of_integers:
        return max(list_of_integers)
    return None
