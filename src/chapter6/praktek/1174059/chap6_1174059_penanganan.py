# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:57:16 2019

@author: Ah elah
"""

def fungsi(npm):
	try:
		import matplotlib.pyplot as plt
		import random as r
		i = (int(npm)%3)+2
		rowcol = ""
		if i%2==0:
			row=i/2
			rowcol=str(int(row))+"2"
		if i%3==0:
			row=i/3
			rowcol=str(int(row))+"3"
		a=1
		while a<=i:
			y = [r.randint(1,10),r.randint(1,10),r.randint(1,10),r.randint(1,10)]
			plt.subplot(int(rowcol+str(4)))
			plt.bar([1,2,3,4], y)
			a+=1
		plt.show()
	except ValueError:
		print("Salah pada index subplot")
	return i
fungsi("1174059")