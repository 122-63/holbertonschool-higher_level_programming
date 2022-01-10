#!/usr/bin/python3
"""
sends a request to the URL and displays the body
- you have to manage urllib.error.HTTPError
- exceptions and print: Error code: followed by the
  HTTP status code
"""
from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as Err:
            print("Error code: {}".format(Err.code))
