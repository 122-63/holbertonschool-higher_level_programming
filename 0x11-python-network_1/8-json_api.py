#!/usr/bin/python3
"""
sends a POST request with the letter as a parameter
"""

from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) == 2:
        arg = argv[1]

    try:
        url = requests.post("b991a1b5a53e.c3bcb5f8.hbtn-cod.io:5000/search_user", data={'q': arg})
        response = url.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
