#!/bin/bash
# Send request to the provided URL and display only the status code
curl -s -I -o /dev/null -w "%{http_code}" "$1"
