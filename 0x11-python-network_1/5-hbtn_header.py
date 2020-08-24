#!/usr/bin/python3
"""Get value of `X-Request-Id` header from requested URL"""
from requests import get
from sys import argv

if __name__ == "__main__":

    try:
        r = get(argv[1])
        print(r.headers.get('X-Request-Id'))
    except Exception as e:
        print(e)
