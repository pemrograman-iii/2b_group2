# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:23:54 2019

@author: Irvan
"""

def nomorTiga(NPM):
    y = NPM[4:7]
    x = NPM[4:5]
    y = NPM[5:6]
    z = NPM[6:7]
    g = (int(x) + int(y) + int(z))
    for i in range(g):
        print('Halo ' + y,'Apa Kabar?')
        
nomorTiga("1174043")