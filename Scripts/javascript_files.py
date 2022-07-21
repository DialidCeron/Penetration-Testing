#!/usr/bin/python3

#Python script that extracts javascript files from access_log.txt file.

import os

os.system("cat access_log.txt | grep '\.js' | cut -d ' ' -f7 | cut -d '/' -f 3 | sort | uniq" )

