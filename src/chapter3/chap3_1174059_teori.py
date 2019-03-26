# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 00:12:23 2019

@author: Ah elah
"""

#1
Fungsi dalam python diartikan sebagai program yang dapat ditugaskan terus menerus tanpa harus mendefinisikannya berulan kali, fungsi selalu didefinisikan dengan \"def\" dengan inputan variabel yang telah disediakan untuk selanjutnya diproses dengan contoh   variabel = input() atau value  dan untuk kembalian variabel yang sudah di proses itu akan menjadi output yang dicontohkan dengan   return variabel  , contoh kode programnya bisa dilihat seperti berikut
def Penambahan(var1,var2)
	var3 = var1+var2
	return var3	
var1 = value1
var2 = value2
var4 = Penambahan(var1,var2)

#2			 
Paket atau library adalah koleksi koleksi dari program yang dapat digunakan dalam membangun struktur program yang lebih rumit. contoh programnya seperti berikut, untuk membuat librarynya seperti ini			 
def Penambahan(var1,var2):
    var3=var1+var2
	return var3
def Pengurangan(var1,var2):
	var3=var1-var2
	return var3
def Perkalian(var1,var2):
    var3=var1*var2
	return var3
def Pembagian(var1,var2):
	var3=var1/var2
	return var3
			 
contoh program pemanggilan librarynya seperti ini
			 
import namafilelibrary
			
var1=value
var2=value
			
var3=namafilelibrary.fungsi1(var1,var2)
var4=namafilelibrary.fungsi2(var1,var2)
var5=namafilelibrary.fungsi3(var1,var2)

#3
Kelas adalah cetakan yang digunakan untuk menciptakan suatu objek, objek adalah segala sesuatu yang nyata maupun abstrak, atribut adalah nilai data yang terdapat dalam objek, dan method adalah apa saja yang dapat dilakukan oleh objek. contoh kode programnya sebagai berikut.
Kelas
			 
class namakelas
	var2 = value1
	
Objek
			 
	var1 = namakelas()
	print(var1.var2) 
			 
atribut
			 
	var1=value1
	var2=value2
			 
method
			 
class namakelas1:
  def __init__(self, var6, var7):
	self.var6 = var6
	self.var7 = var7

  def fungsi4(self):
	print("Hello my name is " + self.var6)

	var8 = namakelas1("John", 36)
	var8.fungsi4()

#4			 
Pemanggilan library dalam python sangat mudah dengan menggunakan keyword \"import\" library otomatis terpanggil, harus diperhatikan, library yang dipanggil harus berada dalam folder yang sama dengan fileprogram yang memanggil library tersebut. contoh programnya sebagai berikut.
			 
import namalibrary
			 
#5
Penggunaan from kalkulator import Penambahan dapat diartikan sebagai pengambilan fungsi penambahan dalam file library beranama kalkulator
			 
from kalkulator import Penambahan
			
var1=value1
var2=value2
var3=Penambahan(var1,var2)
var4=var3.Penambahan()
var5=var3.Pengurangan()
var6=var3.Perkalian()
var7=var3.Pembagian()
			 
#6
import namalibrary 
 
#7
from namalibrary import namafungsi  
		 