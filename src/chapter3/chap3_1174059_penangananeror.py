# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 00:37:29 2019

@author: Ah elah
"""

def penangananeror(NPM):
	try:
		a = int(NPM)
		a = a+4059
		print(str(a))
	except ValueError:
		print("Tidak bisa menggunakan huruf!!")