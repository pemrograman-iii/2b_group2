# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:45:48 2019

@author: Irvan
"""

def nomorDelapan(NPM):
    NPM = list(NPM)
    for x in NPM:
        if int(x) != 0:
            if int(x)%2==0:
                print(x, end = "")
                
nomorDelapan("1174043")