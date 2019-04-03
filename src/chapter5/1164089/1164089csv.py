# In[01]: Import module csv
import csv

# In[02]: Membuat fungsi untuk membaca file csv
def read():
    with open('1164089.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['space'])
            
read()
