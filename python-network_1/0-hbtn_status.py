#!/usr/bin/python3

import urllib.request

with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as response:
    body = response.read()
    print("\t- Body: {}".format(body))
