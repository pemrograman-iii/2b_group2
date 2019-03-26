# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 02:50:06 2019

@author: Muhammad iqbal
"""

def ErrorGais():
	import csv
	try:
		with open('1174063csv.py', newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				print(row['npm'], row['nama'], row['key'])
	except KeyError : 
		print("ERRROOOOORRRRRRR")
        
ErrorGais()