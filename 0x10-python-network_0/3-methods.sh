#!/bin/bash
# Takes in URL, displays all HTTP methods the server will accept.
curl -s -i -X OPTIONS "$1" | grep -i allow | sed 's/Allow" //' | sed 's/, */, /g'
