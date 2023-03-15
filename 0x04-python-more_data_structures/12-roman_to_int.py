#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Given a Roman numeral string 'roman_strin', returns its integer equivalent.
    """
    roman_to_int_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    prev_val = 0
    total_val = 0
    
    for char in roman_string:
        curr_val = roman_to_int_dict[char]
        if curr_val > prev_val:
            total_val -= prev_val
        else:
            total_val += prev_val
        prev_val = curr_val
    total_val += prev_val
    return total_val
