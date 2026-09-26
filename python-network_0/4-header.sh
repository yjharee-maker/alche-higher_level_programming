#!/bin/bash
# Send a GET request with the required header and display the response body
curl -s -H "X-School-User-Id: 98" "$1"
