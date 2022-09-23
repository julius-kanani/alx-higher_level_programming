#!/bin/bash
# Takes a URL, sends GET request to the URL, displays body of response.
curl -fs -X GET "$1"
