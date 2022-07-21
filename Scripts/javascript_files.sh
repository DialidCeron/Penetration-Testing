#!/bin/bash

#Bash script that extracts JavaScript files from the access_log.txt file.

cat access_log.txt | grep "\.js" | cut -d " " -f 7 | cut -d "/" -f 3 | sort | uniq
