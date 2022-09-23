#!/bin/bash
# Takes in URL as argument, sends GET request to URL, displays body response.
curl -s -X GET -H "X-School-User-Id: 98" "$1"
