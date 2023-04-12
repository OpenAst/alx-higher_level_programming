#!usr/bin/python3
"""reads a file and print it on the screen"""

def read_file(filename=""):
    with open("filetext.txt", "r", encoding="utf-8") as f:
        read_data = f.read()
