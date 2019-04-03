# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:18:22 2019

@author: Ah elah
"""

import serial
import csv

def getData():
    ser = serial.Serial('COM6',9600)
    print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
getData()

def writeCsv():
    ser = serial.Serial('COM6',9600)
    with open('sibin.csv', mode='w') as csv_file:
        fieldnames = ['jaraknya']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        while (1):
            data = ser.readline().decode("utf-8").strip('\n').strip('\r')
            writer.writerow({'jaraknya': data})
writeCsv()