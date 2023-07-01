#!/usr/bin/python3
"""
, sends a request to the URL and displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    import urllib.request
    from urllib import error
    import sys

    argv = sys.argv
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as er:
        print("Error code: {}".format(err.status))


