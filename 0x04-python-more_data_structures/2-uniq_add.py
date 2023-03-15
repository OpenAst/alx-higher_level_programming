#!/usr/bin/python3

def uniq_add(my_list=[]):
    number = 0

    for index in set(my_list):
        number += index
    return number
