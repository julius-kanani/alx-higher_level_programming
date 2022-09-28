#!/usr/bin/python3
""" 1-hbtn_header module. Displays value of the X-Request-Id variable. """
import urllib.request
import sys


if __name__ == "__main__":
    ext_url = sys.argv[1]
    with urllib.request.urlopen(ext_url) as response:
        html = response.info()
        print(html['X-Request-Id'])
