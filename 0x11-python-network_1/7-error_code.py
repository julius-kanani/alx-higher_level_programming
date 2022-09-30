#!/usr/bin/python3
""" 7-error_code. Takes in a URL, sends a request to the URL and
    displays the body of the response. """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    result = requests.get(url)
    if result.status_code >= 400:
        print("Error code: {:d}".format(result.status_code))
    else:
        print(result.text)
