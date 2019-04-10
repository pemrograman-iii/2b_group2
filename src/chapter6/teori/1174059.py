#2
from matplotlib import pyplot as plt

plt.plot ([1,2,7],[4,3,9])
plt.show()


#3

#line
from matplotlib import pyplot as plt

x=[1,1,7]
y=[4,5,9]
plt.plot(x,y)
plt.show

#bar
from matplotlib import pyplot as plt

plt.bar([1,3,5,7,9],[20,21,31,33,18],
label="Pisang(Sisir)",color='Y',width=.5)
plt.bar([2,4,6,8,10],[10,12,19,10,15],
label="Rambutan(Kg)", color='K',width=.5)
plt.legend()
plt.xlabel('Minggu')
plt.ylabel('Terjual (buah)')
plt.title('BAR')
plt.show()


#histogram
from matplotlib import pyplot as plt

population_age = [40,12,11,22,16,9,10,15,22,55,62,45,5,22,4,32,35,55,33]
bins = [0,10,20,30,40,50,60,70]
plt.hist(population_age, bins, histtype='bar', rwidth=0.8)
plt.xlabel('Rentan Usia')
plt.ylabel('Jumlah Orang')
plt.title('Histogram')
plt.show()

#scatter
from matplotlib import pyplot as plt

x = [1,1.5,2,2.5,3,3.5,3.9]
y = [7,8.2,8.4,9.6,9.8,10,10.2] 
x1=[8,8.5,9,9.7,10,10.5,10.7]
y1=[3,3.5,3.7,4,4.5,5,5.2]
plt.scatter(x,y, label='Lokasi A',color='B')
plt.scatter(x1,y1,label='Lokasi B',color='R')
plt.xlabel('Penyimpanan(ratus)')
plt.ylabel('Pendapatan(ribu)')
plt.title('SCATTER')
plt.legend()
plt.show()

#stack plot
from matplotlib import pyplot as plt

ari = [1,2,3,4,5,6,7] 
modom =[8,8,6,9,7,8,9]
mangan = [2,3,4,3,2,7,5]
karejo =[7,8,7,6,5,13,2]
marmeam = [7,6,7,8,4,7,15]
potong = [7,2,2,13]
kegiatan = ['modom','mangan','karejo','marmeam']
cols = ['c','m','r','b']

plt.plot([],[],color='m', label='Modom', linewidth=5)
plt.plot([],[],color='c', label='Mangan', linewidth=5)
plt.plot([],[],color='r', label='Karejo', linewidth=5)
plt.plot([],[],color='k', label='Marmeam', linewidth=5)
plt.stackplot(ari,modom,mangan,karejo,marmeam,colors=['m','c','r','b'])
 
plt.xlabel('Hari')
plt.ylabel('Berapa Lama')
plt.title('Stack Plot')
plt.legend()
plt.show()
plt.pie(potong,labels=kegiatan,colors=cols,startangle=0,shadow= True,explode=(0,0,0.1,0),autopct='%1.1f%%')
plt.title('Pie Plot')
plt.show()

#5

import numpy as np
import matplotlib.pyplot as plt

def f(t):
	return np.exp(-t) * np.cos(2*np.pi*t)
	t1 = np.arange(0.0, 5.0, 0.1)
	t2 = np.arange(0.0, 5.0, 0.02)
	plt.subplot(331)
	plt.plot(t1, f(t1), 'bo', t2, f(t2))
	plt.subplot(332)
	plt.plot(t2, np.cos(2*np.pi*t2))
	plt.subplot(333)
	plt.plot(t1, f(t1), 'bo', t2, f(t2))
	plt.subplot(334)
	plt.plot(t2, np.cos(2*np.pi*t2))
	plt.subplot(335)
	plt.plot(t1, f(t1), 'bo', t2, f(t2))
	plt.subplot(336)
	plt.plot(t2, np.cos(2*np.pi*t2))
	plt.subplot(337)
	plt.plot(t1, f(t1), 'bo', t2, f(t2))	
	plt.subplot(338)
	plt.plot(t1, f(t1), 'bo', t2, f(t2))
	plt.subplot(339)
	plt.plot(t2, np.cos(2*np.pi*t2))
	plt.show()
    
#7

import matplotlib.pyplot as plt

x = [9, 13, 11, 12, 41, 21, 25, 35, 40, 45, 10, 50, 53, 29, 22]
num_bins = 5
n, bins, patches = plt.hist(x, num_bins, facecolor='red', alpha=0.5)
plt.show()