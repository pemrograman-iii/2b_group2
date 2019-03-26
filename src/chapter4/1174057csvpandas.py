# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:59:13 2019

@author: alitfajarkurniawan
"""

import pandas
import csv

def readcsv():
    with open('1174057.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t NPM : {row[0]} Nama : {row[1]} Kelas : {row[2]}.')
                line_count += 1
                print(f'Processed {line_count} lines.')

def readdictionary():
    with open('1174057.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t NPM : {row["npm"]} Nama : {row["nama"]} Kelas :  {row["kelas"]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')

def write():
    with open('test-tulis.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(['Kurniawan', 'Manajer', 'Agustus'])
        employee_writer.writerow(['Fajar', 'Staff', 'Desember'])

def readpandas():
    df = pandas.read_csv('1174057.csv')
    print(df)