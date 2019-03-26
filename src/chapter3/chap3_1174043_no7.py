# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:43:26 2019

@author: Irvan
"""

def nomorTujuh(NPM):
    NPM = list(NPM)
    jmlh = 0
    for x in NPM:
        jmlh = jmlh * int(x)
    print("Hasilnya : " +str(jmlh))
    
nomorTujuh("1174043")