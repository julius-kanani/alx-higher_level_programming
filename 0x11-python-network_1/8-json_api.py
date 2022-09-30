#!/usr/bin/python3
""" 8-json_api module. Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter. """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]
    c_data = {'q': letter}

    result = requests.get('http://0.0.0.0:5000/search_user', data=c_data)
    try:
        json_body = result.json()

        if json_body == {}:
            print("No result")
        else:
            print("[{}] {}".format(
                json_body.get("id"), json_body.get("name")))
    except Exception as Error:
        print("Not a valid JSON")
