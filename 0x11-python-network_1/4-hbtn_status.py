#!/usr/bin/python3
# script that fetches https://intranet.hbtn.io/status
from requests import get

if __name__ == "__main__":

    try:
        req = get('https://intranet.hbtn.io/status')
        print("Body response:\n\t- type: {}\n\t- content: {}"
              .format(type(req.text), req.text))
    except Exception as e:
        print(e)
