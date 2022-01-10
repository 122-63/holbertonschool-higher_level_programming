#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the
response (decoded in utf-8) import urllib.request
"""
from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    data = urllib.parse.urlencode(email).encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode("utf-8"))
