# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:38:15 2019

@author: Irvan
"""

def nomorSatu(NPM):
	NPM = int(NPM)
	char = "#"
	if NPM%3 == 0:
		char = "*"
	if NPM%3 == 1:
		char = "#"
	if NPM%3 == 2:
		char = "+"
	baris = []
	baris.append("   ##      ##   ######## ##          #####   ##         #######  ")
	baris.append(" ####    ####   ##    ## ##    ##   ##   ##  ##    ##  ##     ## ")
	baris.append("   ##      ##       ##   ##    ##  ##     ## ##    ##         ## ")
	baris.append("   ##      ##      ##    ##    ##  ##     ## ##    ##   #######  ")
	baris.append("   ##      ##     ##     ######### ##     ## #########        ## ")
	baris.append("   ##      ##     ##           ##   ##   ##        ##  ##     ## ")
	baris.append(" ######  ######   ##           ##    #####         ##   #######  ")   
	a = 0
	for x in baris:
		print(baris[a].replace("#", char))
		a+=1
        
def nomorDua(NPM):
    y = NPM[5:7]
    g = int(y)
    for i in range(g):
        print('Halo ' + NPM,'Apa Kabar?')

def nomorTiga(NPM):
    y = NPM[4:7]
    x = NPM[4:5]
    y = NPM[5:6]
    z = NPM[6:7]
    g = (int(x) + int(y) + int(z))
    for i in range(g):
        print('Halo ' + y,'Apa Kabar?')

def nomorEmpat(NPM):
    y = NPM[4:5]
    print('Halo ' + y,'Apa Kabar?')

def nomorLima(NPM):
    NPM = list(NPM)
    for x in NPM:
        print(x)

def nomorEnam(NPM):
    NPM = list(NPM)
    jmlh = 0
    for x in NPM:
        jmlh = jmlh + int(x)
    print("Hasilnya : " +str(jmlh))

def nomorTujuh(NPM):
    NPM = list(NPM)
    jmlh = 0
    for x in NPM:
        jmlh = jmlh * int(x)
    print("Hasilnya : " +str(jmlh))

def nomorDelapan(NPM):
    NPM = list(NPM)
    for x in NPM:
        if int(x) != 0:
            if int(x)%2==0:
                print(x, end = "")

def nomorSembilan(NPM):
    for x in NPM:
        if int(x) != 0:
            if int(x)%2==1:
                print(x, end = "")

def nomorSepuluh(NPM):
    for x in NPM:
        if int(x) != 0:
            i = 1
            bil = 0
            while i <= int(x):
                if int(x)%i==0:
                    bil+=1
                i+=1
            if bil == 2:
                print(x)