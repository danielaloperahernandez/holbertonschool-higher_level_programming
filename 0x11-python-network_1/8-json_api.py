#!/usr/bin/python3
""" Uses requests module. Prints error code"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    response = requests.post(url, data=data)
    try:
        dic = response.json()
        if not dic:
            print("No result")
        else:
            print("[{}] {}".format(dic.get("id"), dic.get("name")))
    except ValueError:
        print("Not a valid JSON")
