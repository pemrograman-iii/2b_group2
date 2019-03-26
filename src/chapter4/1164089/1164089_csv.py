# In[01]: Dimana akan melakukan import pada library csv
import csv

# In[02]: Membaca file csv dengan mode list
def ReadModeList():
    with open('1164089.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)

# In[03]: Membaca file csv dengan mode dictionary
def ReadModeDict():
    with open('1164089.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)

# In[04]: Menjalankan Fungsi Write atau nebanbah data
def Write():
    with open('1164089CSV.csv', mode='w') as csv_file:
        fieldnames = ['nama', 'kelas', 'daerah asal']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'nama': 'YusniarNS', 'kelas': 'D4TI3C', 'daerah asal': 'Bandung'})
        writer.writerow({'nama': 'ImronS', 'kelas': 'D4TI3C', 'daerah asal': 'Sukabumi'})
