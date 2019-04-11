# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:35:40 2019

@author: Ah elah
"""

def pie(npm):
	import matplotlib.pyplot as plt
	import random as r
	i = (int(npm)%3)+2
	row = ""
	col = ""	
	if i%2==0:
		row=i/2
		col="2"
	if i%3==0:
		row=i/3
		col="3"
	a=1
	labels = 'T', 'B', 'N', 'K'
	fig, axs = plt.subplots(int(row), int(col))		
	while a<=i:
		c=0
		fracs = []			
		wow=0
		while c!=3:
			num = r.randint(1,33)
			wow = wow+num
			fracs.append(num)
			c+=1
		fracs.append(100-wow)
		plt.subplot(str(int(row)),col,a)
		plt.pie(fracs,labels=labels,startangle=90,shadow= True,explode=[0.1,0.1,0.1,0],autopct='%1.1f%%')			
		a+=1		
	plt.show()
	return i
a = pie("1174059")