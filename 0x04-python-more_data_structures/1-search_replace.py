#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to hold the replaced elements
    new_list = []

    # Iterate through the original list
    for element in original_list:
        # If the element is the one to replace, add the replacement element to the new list
        if element == search:
            new_list.append(replace)
        # Otherwise, add the original element to the new list
        else:
            new_list.append(element)

    # Return the new list with replaced elements
    return new_list

