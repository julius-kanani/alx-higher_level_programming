#!/usr/bin/python3
""" 3-error_code module. takes in a URL, sends a request to the URL,
    and displays the body of the response (decoded in utf-8). """
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            result = response.read()
            print(result.decode("ascii"))
    except urllib.error.URLError as Error:
        print("Error code: {:d}".format(Error.code))
