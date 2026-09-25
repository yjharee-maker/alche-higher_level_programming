#!/bin/bash
# Get URL, send a request to that URL and display the size of the response's body.
curl -s -o /dev/null -w '%{size_download}' "$1"
