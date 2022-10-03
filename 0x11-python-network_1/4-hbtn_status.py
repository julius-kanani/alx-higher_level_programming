#!/usr/bin/python3
""" 4-hbtn_status module. fetches https://alx-intranet.hbtn.io/status. """
import requests


if __name__ == "__main__":
    result = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(result.text)))
    print("\t- content: {:s}".format(result.text))
