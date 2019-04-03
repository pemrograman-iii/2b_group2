# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 01:13:52 2019

@author: Ah elah
"""

import csv



def macacsv():
    with open('sibin.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['jaraknya'])
macacsv()