#!/usr/bin/python3
"""Post an email address to the requested URL"""
from requests import post
from sys import argv

if __name__ == "__main__":

    try:
        res = post(argv[1], data={'email': argv[2]})
        print(res.text)
    except Exception as e:
        print(e)
