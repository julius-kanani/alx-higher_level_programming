#!/usr/bin/python3
""" 4-hbtn_status module. fetches https://alx-intranet.hbtn.io/status. """
import requests


if __name__ == "__main__":
    result = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response: ")
    print("    - type: <class 'str'>")
    print("    - content: {:s}".format(result.text))
