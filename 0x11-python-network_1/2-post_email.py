#!/usr/bin/python3
""" 2-post_email module. Takes in a URL, and an email, sends a POST
    request to the passed URL with the email as a parameter, and displays
    the body of the response. (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    ext_url = sys.argv[1]
    email = sys.argv[2]

    # Encode the data object into a string
    data = urllib.parse.urlencode({'email': email})

    # Set the encoding scheme on the string data object
    data = data.encode('utf-8')

    req = urllib.request.Request(ext_url, data)

    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("Your email is: {:s}".format(html.decode('utf-8')))
