#!/usr/bin/python3
"""This module adds all arguments to a Python list and saves them to a file."""

import sys
from typing import List

def add_items_to_list_and_save(items: List[str], filename: str) -> None:
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        current_items = load_from_json_file(filename)
    except FileNotFoundError:
        current_items = []

    updated_items = current_items + items
    save_to_json_file(updated_items, filename)

if __name__ == "__main__":
    args = sys.argv[1:]
    add_items_to_list_and_save(args, "add_item.json")

