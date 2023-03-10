#!/usr/bin/python3

def no_c(my_string):
    changed_str = ''

    for i in my_string:
        if i != 'c' and i != 'C':
            changed_str += i
    return (changed_str)
