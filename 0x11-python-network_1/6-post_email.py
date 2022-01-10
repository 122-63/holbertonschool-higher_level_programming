#!/usr/bin/python3
"""
POST - email - requests
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    data = requests.post(url, email)
    print(data.text)
