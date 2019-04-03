# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 01:11:39 2019

@author: Ah elah
"""

import serial

arduino = serial.Serial('COM6',9600) 
def sensorjarak():
	data = int(arduino.readline())
	print(data)

try:
	while (True):
		sensorjarak()
except KeyboardInterrupt:
	arduino.close()
	print('Sebentar aja cukup ^_^')