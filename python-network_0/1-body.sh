#!/bin/bash
# Display the body if response code is 200
curl -sL -o /tmp/body -w '%{http_code}' "$1" | grep -q '^200$' && cat /tmp/body
