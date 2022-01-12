#!/usr/bin/python3
"""
Github id
"""
import requests
from sys import argv


if __name__ == "__main__":


    URL = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    req = requests.get(URL, auth=(username, password))
    x = req.json()
    print(x.get('id'))