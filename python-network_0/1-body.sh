#!/bin/bash
# Display the body if response code is 200
curl -s -w '%{http_code}' "$1" | grep -q 200 && curl -s "$1"
