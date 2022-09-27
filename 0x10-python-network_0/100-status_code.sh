#!/usr/bin/env bash
# Returns only a status code
curl -sI -o /dev/null -w "%{http_code}" "$1"
