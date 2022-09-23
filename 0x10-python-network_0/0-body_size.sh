#!/bin/bash
# Takes in a URL, sends request to URL, displays size of body of response.
curl -Is "$1" | grep "Content-Length" | cut -d " " -f 2
