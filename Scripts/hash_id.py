#!/usr/bin/python
# -*- coding: utf-8 -*-
#Cerón Rodríguez Lezly Dialid
#Programa para identificar tipos de hashes
#Uso: Cadena como argumento

from builtins import input
from sys import argv, exit

print("**********************************************")
print("*             Identificador de hashes        *")
print("*                  Por Dialid                *")
print("**********************************************")

algoritmos={"1":"MD2", "2":"MD4", "3":"MD5", "4":"RIPEMD-128", "5":"RIPEMD-160", "6":"SHA1", "7":"SHA-224", "9":"SHA-256", "10":"RIPEMD-320", "11":"SHA-384", "12":"SHA-512", "13":"Whirlpool"}

def MD2(hash):
	hs='08bbef4754d98806c373f2cd7d9a43c4'
	if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
		possib.append("1")
def MD4(hash):
	hs='a2acde400e61410e79dacbdfc3413151'
	if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
		possib.append("2")

def MD5(hash):
	hs='6be20b66f2211fe937294c1c95d1cd4f'
	if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
		possib.append("3")

def RipeMD128(hash):
	 hs='4985351cd74aff0abc5a75a0c8a54115'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
    	possib.append("4")

def RipeMD160(hash):
    hs='dc65552812c66997ea7320ddfb51f5625d74721b'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
    	possib.append("5")

def SHA1(hash):
    hs='4a1d4dbc1e193ec3ab2e9213876ceb8f4db72333'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
    	possib.append("6")
try:
	first=str(argv[1])
except:
	first=None

while True:
	try:
		possib=[]
		print("-"*50)
		if first:
			h=first
		else:
			h=input(" HASH: ")
		MD2(h)
		if len(possib)==0:
			print("Hash no encontrada.")
		else:
			print("\nPosibles Hashes:")
			for a in range(len(possib)):
				print("[+]"+str(algoritmos[possib[a]]))

		first=None
	except KeyboardInterrupt:
		print("\nBye!")
		exit()
