# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:59:17 2019

@author: Irvan
"""

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
                
nomorSepuluh("1174043")