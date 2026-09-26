#!/usr/bin/python3
"""Fetches and displays the status of a URL using urllib."""

import urllib.request

with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as response:
    body = response.read()
    print("\t- Body: {}".format(body))
