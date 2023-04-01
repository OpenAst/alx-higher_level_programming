#!/usr/bin/python3

add_integer = __import__("0-add_integer").add_integer
print(add_integer(2, 5))
print(add_integer(100, -4))
print(add_integer(4))
print(add_integer(24.4, 6))

try:
    print(add_integer(4, "Holberton"))
except Exception as f:
    print(f)

try:
    print(add_integer(None))
except Exception as e:
    print(e)


