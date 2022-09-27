#!/bin/bash
# Returns only a status code
curl -s "{$1}" -X POST -H "Content-Type: application/json" -d @$2
