#!/usr/bin/python3
"""This module sends a request to a URL and displays the response body."""

import urllib.request

with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as response:
    body = response.read()
    print("\t- Body: {}".format(body))
