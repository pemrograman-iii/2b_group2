# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:36:07 2019

@author: Irvan
"""

def nomorEnam(NPM):
    NPM = list(NPM)
    jmlh = 0
    for x in NPM:
        jmlh = jmlh + int(x)
    print("Hasilnya : " +str(jmlh))
    
nomorEnam("1174043")