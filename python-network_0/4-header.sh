#!/bin/bash
# Send a GET request with the required header and display the response body
curl -s --header "X-HolbertonSchool-User-Id: 98" "$1"
