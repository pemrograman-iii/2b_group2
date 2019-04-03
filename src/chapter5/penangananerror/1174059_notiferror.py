# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 01:24:03 2019

@author: Ah elah
"""

import serial



def panggil():
    try:
        ser = serial.Serial('COM6',9600)
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
    except SyntaxError:
        print("Kesalahan penulisan syntax")
    except NameError:
        print("Variable tersebut tidak ada")
    except TypeError:
        print("Tipe data salah")
panggil()