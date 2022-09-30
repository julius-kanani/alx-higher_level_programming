#!/usr/bin/python3
""" 5-hbtn_header module. Response Header value. """
import requests
import sys


if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io")
    print(req.headers['X-Request-Id'])
