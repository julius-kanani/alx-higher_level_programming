#!/bin/bash
# Takes in URL, displays all HTTP methods the server will accept.
curl -sIX OPTIONS 127.0.0.1:80 | grep "Allow" | cut -d " " -f2 | sed 's/,/, /g'
