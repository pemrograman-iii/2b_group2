##No 1##
def Penambahan(a, b): #Inisiasi Fungsi dan Inputan Fungsi
	c = a+b 
	return c #Pengembalian Fungsi

##No 2##
import kalkulator #Pemanggilan biasa
import kalkulator as kal #Pemanggilan dengan inisial

##No 3##
#File Kalkulator.py
class kalkulator: #Kalkulator merupakan class
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def Penambahan(self): #a dan b merupakan atribut, Penambahan merupakan fungsi
		coba = self.a+self.b #Coba merupakan atribut
		print(str(coba))

#File main.py
import Kalkulator

kal = Kalkulator.Kalkulator(1, 2) #Berikut merupakan objek
kal.penambahan()

##No 4##
import Kalkulator

kal = Kalkulator

##No 5##
from Kalkulator import Penambahan

coba = Penambahan(1, 2)

##No 6##
import  Kalkulator
hasil1 = Kalkulator.Penambahan(1, 2)
print(str(hasil1))

##No 7##
import Kalkulator

kal = Kalkulator.kalkulator(1,2)
hasil1 = kal.Penambahan()
print(str(hasil1))