# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:53:00 2019

@author: Irvan
"""

def nomorSembilan(NPM):
    for x in NPM:
        if int(x) != 0:
            if int(x)%2==1:
                print(x, end = "")
                
nomorSembilan("1174043")