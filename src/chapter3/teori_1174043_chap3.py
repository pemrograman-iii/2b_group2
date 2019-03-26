##No 1 Teori
def LuasPersegi(s): ##pendefinisian Fungsi
	x = s * s
	return x ##Nilai kembalian fungsi
print("Masukkan Sisi Persegi = ")
sisi = input() ##Fungsi input
s = int(sisi)
print(LuasPersegi(s))

##No 2 Teori
import kalkulator

##No 3 Teori
class MyClass: ##pendefinisian Kelas
	a = 10 ##atribut
	def func(self): ##method
		print('Hello')
		
ob = MyClass() ##objek

##No 4 Teori
import kalkulator

a = kalkulator ##instansiasi library kelas

##No 5 Teori
from kalkulator import penambahan, pengurangan

##No 6 Teori
import kalkulator
a = 10
b = 20

c = kalkulator.penambahan(a,b)
print(c)

##No 7 Teori
import kalkulator

x = kalkulator.Hitung(3,4)
hasil = x.Penambahan()
print(str(hasil))
