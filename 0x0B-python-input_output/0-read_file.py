#!usr/bin/python3
"""reads a file and print it on the screen"""

def read_file(filename=""):
    """prints the content of a text file"""
    with open("filetext.txt", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
