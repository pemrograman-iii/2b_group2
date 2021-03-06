# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:38:47 2019

@author: alitfajarkurniawan
"""

import csv

#Jawaban No. 1
def bukaModeListCsv():
    with open('teori_alit.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])

#Jawaban No. 2            
def bukaModeDictCsv():
    with open('teori_alit.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])

def tulisCsv():
    with open('teori6_alit.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1174099', 'nama': 'Justin', 'kelas': 'D4TI2A', 'tanggal lahir': '05/05/1999'})
        writer.writerow({'npm': '1174055', 'nama': 'Steven', 'kelas': 'D4TI2B', 'tanggal lahir': '06/06/1999'})
