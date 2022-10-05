#!/usr/bin/python3
""" Takes Github credentials (username and password) and uses the GitHub API
    to display user ID. """
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username, passwd = sys.argv[1], sys.argv[2]
    url = "https://api.github.com/user"
    basic_auth = HTTPBasicAuth(username, passwd)

    response = requests.get(url, auth=basic_auth)
    print(response.json().get('id'))
