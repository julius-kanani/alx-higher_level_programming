#!/usr/bin/python3
""" 5-hbtn_header module. Response Header value. """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers['X-Request-Id'])
