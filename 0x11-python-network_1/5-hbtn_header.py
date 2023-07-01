#!/usr/bin/python
"""
 Python script that takes in a URL, sends a request to 
 the URL and displays the value of the variable X-Request-Id
"""


if __name__ == "__main__":
    import sys
    from requests import get

    result = get(argv[1])
    print(result.headers.get('X-Request-Id'))

