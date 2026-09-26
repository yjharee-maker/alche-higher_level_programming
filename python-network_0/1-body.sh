#!/bin/bash
# Display the body if response code is 200
status=$(curl -s -o /tmp/curl_body -w '%{http_code}' "$1")
if [ "$status" = "200" ]; then cat /tmp/curl_body fi
