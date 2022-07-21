#!/bin/bash

#Bash script that performs a ping sweep of the IP range 10.11.1.0/24

for ip in $(seq 1 254);
do
	ping -c 1 10.11.1.$ip | grep "64 bytes" | cut -d " " -f 4 | cut -d ":" -f 1
done
