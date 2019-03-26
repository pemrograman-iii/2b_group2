class fthr:
	def __init__(self, a, b):
	    self.a = a
        self.b = b
    def tambah(self):
        r = self.a + self.b
        return r

def coba():
    print("coba")
coba()

def coba2(nm):
    print("Namaku :"+str(nm))
coba2(input("NAMA:"))

def coba3(a,b):
	x = a+b
	return x

a = 7
b = 5
y = coba3(a,b)
print(y)

#1
def coba4(n):
    n = list(str(n))
    
    angka1 = {"0":" ######### ","1":" ### ","2":" ###### ","3":" ####","4":" ###   ### ","5":" ########## ","6":" ###### ","7":" ########### ","8":" ###### ","9":" ###### "}
    angka2 = {"0":" ######### ","1":" ### ","2":" ###### ","3":" ####","4":" ###   ### ","5":" ########## ","6":" ##  ## ","7":" ########### ","8":" ##  ## ","9":" ##  ## "}
    angka3 = {"0":" ##     ## ","1":" ### ","2":"     ## ","3":"   ##","4":" ###   ### ","5":" ###        ","6":" ##     ","7":"        ###  ","8":" ##  ## ","9":" ##  ## "}
    angka4 = {"0":" ##     ## ","1":" ### ","2":"     ## ","3":"   ##","4":" ###   ### ","5":" ###        ","6":" ##     ","7":"       ###   ","8":" ##  ## ","9":" ##  ## "}
    angka5 = {"0":" ##     ## ","1":" ### ","2":" ###### ","3":" ####","4":" ######### ","5":" ########## ","6":" ###### ","7":"      ###    ","8":" ###### ","9":" ###### "}
    angka6 = {"0":" ##     ## ","1":" ### ","2":" ###### ","3":" ####","4":"       ### ","5":" ########## ","6":" ###### ","7":"     ###     ","8":" ###### ","9":" ###### "}
    angka7 = {"0":" ##     ## ","1":" ### ","2":" ##     ","3":"   ##","4":"       ### ","5":"        ### ","6":" ##  ## ","7":"    ###      ","8":" ##  ## ","9":"     ## "}
    angka8 = {"0":" ##     ## ","1":" ### ","2":" ##     ","3":"   ##","4":"       ### ","5":"        ### ","6":" ##  ## ","7":"   ###       ","8":" ##  ## ","9":"     ## "}
    angka9 = {"0":" ######### ","1":" ### ","2":" ###### ","3":" ####","4":"       ### ","5":"  ######### ","6":" ##  ## ","7":"  ###        ","8":" ##  ## ","9":" ##  ## "}
    angka10 = {"0":" ######### ","1":" ### ","2":" ###### ","3":" ####","4":"       ### ","5":"  ######### ","6":" ###### ","7":" ###         ","8":" ###### ","9":" ###### "}
                      
    hasil1 = []
    hasil2 = []
    hasil3 = []
    hasil4 = []
    hasil5 = []
    hasil6 = []
    hasil7 = []
    hasil8 = []
    hasil9 = []
    hasil10 = []
    
    for x in n:
        hasil1.append(angka1[x])
        hasil2.append(angka2[x])
        hasil3.append(angka3[x])
        hasil4.append(angka4[x])
        hasil5.append(angka5[x])
        hasil6.append(angka6[x])
        hasil7.append(angka7[x])
        hasil8.append(angka8[x])
        hasil9.append(angka9[x])
        hasil10.append(angka10[x])
    
    print(*hasil1, sep=' ')
    print(*hasil2, sep=' ')
    print(*hasil3, sep=' ')
    print(*hasil4, sep=' ')
    print(*hasil5, sep=' ')
    print(*hasil6, sep=' ')
    print(*hasil7, sep=' ')
    print(*hasil8, sep=' ')
    print(*hasil9, sep=' ')
    print(*hasil10, sep=' ')
coba4(input("NPM:"))

#2
def loop(n):
    calc = 0
    while(calc < 74):
        print("Hello, "+str(n)+" Apa Kabar?")
        calc = calc +1
loop(int(input("NPM:")))

#3
def loop3(x):
    y = 0
    a = int(x[4])
    b = int(x[5])
    c = int(x[6])
    d = x[4:7]
    e = a+b+c
    while y < e:
        y += 1
        print("Hello, " + d + " Apa Kabar?")
    return x
loop3(input("NPM:"))

#4
def value4(x):
    n = x[4]
    print("Hello, " + n + " Apa Kabar?")
    return x
value4(input("NPM:"))

#5
def loopdown(x):
    for i in x:
        print(i)
    return i
loopdown(input("NPM:"))

#6
def tambah(n):
    hasil = 0
    for i in n:
        hasil += int(i)
    print(str(hasil))

tambah(input("NPM:"))

#7
def kali(n):
    hasil = 0
    for i in n:
        hasil *= int(i)
    print(str(hasil))

kali(input("NPM:"))

#8
def nilaigenap(x):
    npm = [a,b,c,d,e,f,g]

    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end ="")
nilaigenap(input("NPM:"))

#9
def nilaiganjil(x):
    npm = [a,b,c,d,e,f,g]

    for n in npm:
        if(n % 2 != 0):
            print(n, end ="")
nilaiganjil(input("NPM:"))

#10
def prim(x):
    npm = [a,b,c,d,e,f,g]

    for n in npm:
        if(n % 2) == 0:
            print(end="")
        else:
            print(n, end ="")
prim(input("NPM:"))

#error
def error(a,b):
    try :
        c = a+b
        print(c)
    except TypeError:
        print("We Are Different")
a = 10
b = 2

#paket
def tambah2(a,b):
    r = a+b
    return r

import praktek
a = 1
b = 3
c = praktek.tambah2(a,b)

#pemanggilan
import fthr

a = 1
b = 3
c = lib.fthr(a,b)
result=c.tambah2()

#library kalkulator
def penambahan(a,b):
    r = a+b
    return r

from kalkulator import penambahan

a = 1
b = 3

result = penambahan(a,b)

import kalkulator
a = 1
b = 3
result = kalkulator.penambahan(a,b)

