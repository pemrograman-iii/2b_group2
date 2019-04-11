# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:23:29 2019

@author: Ah elah
"""

def bar(npm):
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
		plt.subplot(int(rowcol+str(a)))
		plt.bar([1,2,3,4], y)
		a+=1	
	plt.show()
	return i
bar("1174059")