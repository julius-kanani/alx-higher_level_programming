#!/bin/bash
# Takes in URL, displays all HTTP methods the server will accept.
curl -sIX OPTIONS "$1" | grep "Allow" | cut -d " " -f 2
