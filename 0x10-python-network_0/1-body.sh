#!/bin/bash
# Takes a URL, sends GET request to the URL, displays body of response.
curl -fLs -X GET "$1"
