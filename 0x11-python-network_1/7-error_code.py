#!/usr/bin/python3
"""
If the HTTP status code is greater than or equal to 400, print: Error code:
You must use the packages requests and sys
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
