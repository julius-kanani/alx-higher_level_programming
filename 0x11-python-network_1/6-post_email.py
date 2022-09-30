#!/usr/bin/python3
""" 6-post_email module. Takes in a URL and an email address, sends a
    POST request to the passed URL with the email as a parameter,
    and finally displays the body of the response. """
import requests
import sys


if __name__ == "__main__":
    # Get user email and the URL to visit.
    url, email = sys.argv[1], sys.argv[2]

    # Send a POST request
    result = requests.post(url, data={'email': email})

    # Display the body of the response
    print(result.txt)
