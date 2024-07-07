#!/bin/bash
# Send request and display status code
curl -s -o /dev/null -w "%{http_code}\n" "$1"
