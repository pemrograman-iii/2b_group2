# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:23:55 2019

@author: Ah elah
"""

import serial



def LOOP():
    ser = serial.Serial('COM6',9600)
    while (1):
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
LOOP()