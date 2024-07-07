#!/bin/bash
# Display only the status code of the response for a given URL.
curl -s -o /dev/null -w "%{http_code}" "$1"
