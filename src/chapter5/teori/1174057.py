# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:59:08 2019

@author: alitfajarkurniawan
"""
import serial

def cobaarduino():
	ser = serial.Serial("COM10",9600)
	print(ser.name)

cobaarduino()
