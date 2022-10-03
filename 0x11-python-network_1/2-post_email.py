#!/usr/bin/python3
""" 2-post_email module. Takes in a URL, and an email, sends a POST
    request to the passed URL with the email as a parameter, and displays
    the body of the response. (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]
    value = {"email": email}
    data = urllib.parse.urlencode(value)

    # data should be in bytes
    data = data.encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        received_email = response.read()
        print(received_email.decode("utf-8"))
