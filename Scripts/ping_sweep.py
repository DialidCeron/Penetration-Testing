#!/usr/bin/python3

#Python script to perform a ping sweep of the IP range 10.11.10/24

import os

def ping(host):
	alive = os.system("ping -c 1 " + host + " > /dev/null")
	if alive==0:
		return host;
	else:
		return "notalive";

for i in range(1,255):
	result = ping("10.11.1." + str(i))
	if(result!='notalive'):
		print(result);
